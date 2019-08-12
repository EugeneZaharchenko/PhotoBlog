from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, unique=False, blank=False, verbose_name="Имя")
    surname = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="Фамилия")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата регистрации")

    def __str__(self):
        return "{name}".format(name=self.name)

    def __repr__(self):
        return "{name}".format(name=self.name)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


