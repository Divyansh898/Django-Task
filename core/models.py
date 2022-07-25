from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile = models.ImageField(default='img/user.png',upload_to='img')
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    is_doctor = models.BooleanField(default=False)
    is_patients = models.BooleanField(default=False)


    def __str__(self):
        return self.username
