from django.db import models
from blog.models import Category
from django_countries.fields import CountryField
from django_countries import countries


class Strana(models.Model):
    country_choices = countries

    COUNTRY = CountryField(choices=country_choices, verbose_name="Страна")

    def __str__(self):
        return str(self.COUNTRY)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Photo(models.Model):
    image = models.ImageField(upload_to="photos", error_messages={
        "required": "It is required field",
        "invalid_image": "It is wrong image format"
    })
    # label = "Photo",
    description = models.CharField(max_length=255, null=True)
    # category = models.ForeignKey(Category)
    country = models.ForeignKey(Strana, default=None, on_delete=models.CASCADE)
    # post = models.OneToOneField('blog.Post', default=None, unique=True, primary_key=True)

    def __str__(self):
        return self.description
