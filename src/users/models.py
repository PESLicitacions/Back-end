# Create your models here.
from sqlite3 import IntegrityError
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User
from licitacions.models import Localitzacio

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Email can not be null.')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        try:
            user.save(using=self._db)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e) and 'username' in str(e):
                raise ValueError('Username already exists.')
            elif 'UNIQUE constraint' in str(e) and 'email' in str(e):
                raise ValueError('Email already exists.')
            else:
                raise e
        return user
      
class CustomUser(AbstractUser):
    #custom fields
    email = models.EmailField(verbose_name='email address', unique=True, blank=False)
    username = models.TextField(max_length=30, unique=True, blank=False)
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
