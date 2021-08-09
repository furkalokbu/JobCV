from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class UserAdmin(UserAdmin):
    model = CustomUser
    
