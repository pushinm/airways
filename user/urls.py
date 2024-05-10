from django.urls import path
from .views import RegisterAPIView, ActivateAPIView, CustomAuthToken, update_profile

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/', ActivateAPIView.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('update/', update_profile),
]