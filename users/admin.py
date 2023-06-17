from django.contrib import admin

from django.conf import settings
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
	list_display=['pk','first_name','last_name','username','email']
