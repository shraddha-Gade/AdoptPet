from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    contact_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True, default='')

    groups = models.ManyToManyField(Group, related_name='customuser_set', related_query_name='customuser')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', related_query_name='customuser')
