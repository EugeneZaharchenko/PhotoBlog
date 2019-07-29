from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, unique=False, blank=False)
    surname = models.CharField(max_length=100, unique=True, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "User {name}".format(name=self.name)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


