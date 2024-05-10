from rest_framework.views import APIView
from .models import MyUser, Activation, Profile
from .serializers import *
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from booking.models import State
# from django.contrib.auth import authenticate


class RegisterAPIView(APIView, UpdateModelMixin):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            activation = Activation.objects.create(user=user)
            # create Activation object here and send it to email
            # self._send_email_verification(user, activation.code)
            return Response({
                "user": serializer.data,
                "success": "True",
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def _send_email_verification(self, user: MyUser, code):
    #     current_site = get_current_site(request=self.request)
    #     subject = 'Activate your profile'
    #
    #     body = render_to_string(
    #         'emails/email_verification.html',
    #         {
    #             'domain': current_site.domain,
    #             'activation_code': code,  # Include activation code in the email
    #         }
    #     )
    #     EmailMessage(to=[user.email], subject=subject, body=body).send()


# @method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for this view
class ActivateAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        print(email)
        password = request.data.get('password')
        print(password)
        activation_code = request.data.get('activation_code')
        print(activation_code)
        # Check if user exists with the given email
        try:
            user = MyUser.objects.get(email=email)
            if not user.check_password(password):
                return Response({'error': "incorrect credetentials. (password)"}, status=status.HTTP_400_BAD_REQUEST)
        except user.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the activation code matches
        activation = Activation.objects.filter(user=user, code=activation_code).first()
        if not activation:
            return Response({"error": "Invalid activation code."}, status=status.HTTP_400_BAD_REQUEST)

        # Activate user
        user.is_active = True
        user.save()

        return Response({"message": "User activated successfully."}, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):
    serializer_class = MyUserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        print(token)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })



@api_view(['PUT'])
def update_profile(request):
    auth_header = request.headers.get('Authorization')

    if auth_header is not None:
        token_string = auth_header.split(' ')[1]
    else:
        return Response({"detail": "Authorization header not provided"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        token = Token.objects.get(key=token_string)
        request.user = token.user
        print(request.user)
    except Token.DoesNotExist:
        return Response({"detail": "Token is invalid"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        profile = request.user.user_profile
        print('profile True')
    except Profile.DoesNotExist:
        return Response({"error": "Profile does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        print('ser True')
        if serializer.is_valid():
            # Update only the photo and full name fields
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
