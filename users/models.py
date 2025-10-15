from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    phone= models.CharField(max_length=11)
    date_of_birth = models.DateField()

    REQUIRED_FIELDS = ["date_of_birth", "phone"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
