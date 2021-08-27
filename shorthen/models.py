from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

from django.contrib.auth.models import AbstractUser
from django.db.models.fields.reverse_related import OneToOneRel

class User(AbstractUser):
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=255,null=True,blank=True)


class UrlWithAccount(models.Model):
    url = models.URLField(max_length=255)
    shorthen_link_id = models.CharField(max_length=255,unique=True)
    date = models.DateTimeField(auto_now_add=True)
    seen = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class UrlWithoutAccount(models.Model):
    url = models.URLField(max_length=255)
    shorthen_link_id = models.CharField(max_length=255,unique=True)
    date = models.DateTimeField(auto_now_add=True)