from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from .models import User

# محل قرار گیری سطح دسترسی کاربر ویژه در پنل مدیریت 
UserAdmin.fieldsets[2][1]['fields'] = (
										'is_active', 
										'is_staff', 
										'is_superuser', 
										'is_author', 
										'special_user', 
										'groups', 
										'user_permissions'
									)
UserAdmin.list_display += ('is_author', 'is_special_user')

admin.site.register(User, UserAdmin)

# Create your models here.
