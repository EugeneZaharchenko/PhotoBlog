
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", unique=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ключевые слова")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.ForeignKey(Category, default=None, verbose_name="Категория")
    img = models.ImageField(null=True, upload_to="posts", verbose_name="Картинка")
    tag = models.ManyToManyField(Tag)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


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

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
