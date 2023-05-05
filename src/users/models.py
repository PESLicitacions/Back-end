# Create your models here.
'''
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email or not password or not extra_fields.get('name'):
            raise ValueError('All the fields must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
'''


    
    

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings


from django.contrib.auth.models import User
from django.forms import ValidationError
from licitacions.models import Localitzacio


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email can not be null.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
class CustomUser(AbstractUser):
    pass

    #custom fields
    email = models.EmailField(verbose_name='email address', unique=True)
    username = None
    name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=310, blank=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    

class Perfil(models.Model):
    CIF = models.TextField(primary_key=True, max_length=10)
    tipus_id = models.TextField(null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    descripcio = models.TextField(null=True)
    localitzacio = models.TextField(null=True)
    cp = models.TextField(null=True)
    telefon = models.TextField(null=False)
    idioma = models.TextField(null=False)


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='follower')
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='following')
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['follower', 'following'], name='unique_follow'
            )
        ]