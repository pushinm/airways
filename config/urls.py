"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="TOYOTA AIRWAYS",
        default_version='v1',
        description="SALIKH KRASAVCHIK",
        terms_of_service="https://salikhdev.clinic.uz/v1/",
        contact=openapi.Contact(email="salikhdev@gmail.com"),
        # license=openapi.License(name="Your License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,)
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls')),
    path('flights/', include('booking.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]
