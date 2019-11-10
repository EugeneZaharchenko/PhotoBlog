from django.db import models
from django.utils import timezone
from users.models import CustomUser
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", unique=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=100, unique=True, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания")
    published_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата публикации")
    category = models.ForeignKey(Category, default=None, verbose_name="Категория", on_delete=models.CASCADE)
    img = models.ImageField(blank=True, upload_to="posts", verbose_name="Картинка", default=None)
    # tags = TaggableManager()
    # tag = models.ManyToManyField(Tag, verbose_name="Тег")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE, verbose_name="Пост")
    author = models.CharField(max_length=200, verbose_name="Комментатор")
    text = models.TextField(verbose_name="Текст")
    mail = models.EmailField(null=False, default=None, verbose_name="Электронный адрес")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата комметария")
    approved_comment = models.BooleanField(default=False, verbose_name="Одобрен")

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
