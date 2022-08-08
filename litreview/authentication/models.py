from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    avatar = models.ImageField(
        upload_to='', 
        blank = True, 
        verbose_name='Photo de profil'
        )
