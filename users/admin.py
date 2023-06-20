from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

UserAdmin.fieldsets+=(('custom info',{'fields':('profile_image',)}),)
UserAdmin.list_display+=('profile_image','pk')
admin.site.register(get_user_model(), UserAdmin)