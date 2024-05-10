from django.contrib import admin
from .models import MyUser, Activation, Profile
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Activation)
admin.site.register(Profile)