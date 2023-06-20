from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	email=models.EmailField(unique=True)
	profile_image=models.ImageField(blank=True,null=True,upload_to='profile/%Y/%m/')
	is_author=models.BooleanField(default=False)