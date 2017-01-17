
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from django_countries import countries


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", unique=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Strana(models.Model):
    country_choices = countries

    COUNTRY = CountryField(choices=country_choices, verbose_name="Страна")

    def __str__(self):
        return str(self.COUNTRY)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    country = models.ForeignKey(Strana, default=None)
    category = models.ForeignKey(Category, default=None, verbose_name=_("Category"))
    # img = models.ImageField(upload_to="posts", verbose_name=_("Post Image"))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")


class Comment(models.Model):

    GENDER_CHOICES = (('male', 'Мужчина'), ('female', 'Женщина'), ('it', 'не знаю'))

    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, default='it')
    text = models.TextField()
    mail = models.EmailField(null=False, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
