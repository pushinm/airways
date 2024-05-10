from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import MyUser, Profile
from booking.models import State
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = MyUser
        fields = ('email', 'password')
        extra_kwargs = {
            'email': {'required': True},
        }

    def create(self, validated_data):
        user = MyUser.objects.create(
            email=validated_data['email'],
            is_active=True  # AFTER OTP TURN IT INTO FALSE
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ActivateSerializer(serializers.Serializer):
    activation_code = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class MyUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        print(email)
        password = data.get('password')
        print(password)

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            print(f'{user}')
            if user is None:
                raise serializers.ValidationError("Invalid email/password. Please try again.")

            if not user.is_active:
                raise serializers.ValidationError("User is deactivated.")

        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        data['user'] = user
        return data


class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name')

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'phone_number', 'full_name']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})  # Get user data if provided
        user = instance.user  # Get the related user object

        # Update the related user's full name if provided
        user.full_name = user_data.get('full_name', user.full_name)
        user.save()

        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'statename']
