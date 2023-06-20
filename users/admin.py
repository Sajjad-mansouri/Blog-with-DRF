from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

UserAdmin.fieldsets+=(('custom info',{'fields':('profile_image',)}),)
UserAdmin.fieldsets[2][1]['fields']=('is_active', 'is_staff', 'is_superuser','is_author', 'groups', 'user_permissions')
UserAdmin.list_display+=('profile_image','pk')
admin.site.register(get_user_model(), UserAdmin)