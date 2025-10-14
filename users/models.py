from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    phone= models.CharField(max_length=11)
    date_of_birth = models.DateField()

    REQUIRED_FIELDS = ["date_of_birth", "phone"]
