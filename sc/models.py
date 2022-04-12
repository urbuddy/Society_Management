from django.db import models
from django.contrib.auth.models import AbstractUser
from .Manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=14)
    flat_no = models.IntegerField(default=0)
    tower_no = models.IntegerField(default=0)
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Notice(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)


class Complaint(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)

