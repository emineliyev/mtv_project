from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

from mtv import settings


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Başlıq')
    description = models.TextField(verbose_name='Məzmun')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL, related_name='post_author', verbose_name='Müəllif')
    image = models.ImageField(upload_to="image/post/%Y/%m/%d/", null=True, blank=True, verbose_name='Şəkil',
                              help_text='Xəbər üçün şəkil ölçüsü 1000X850')
    category = TreeForeignKey('Category', on_delete=models.CASCADE, related_name='post_category', verbose_name='Kateqoriya')
    tag = models.ManyToManyField('Tag', related_name='post_tags', verbose_name='Teq')
    view = models.PositiveIntegerField(default=0, verbose_name='Baxış sayı')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Yayım tarixi')
    published = models.BooleanField(default=False, verbose_name='Aktivlik')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Xəbər'
        verbose_name_plural = 'Xəbər'
        ordering = ['-create_at']


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Kateqoriyanın adı')
    slag = models.SlugField(unique=True, max_length=250, verbose_name='Kateqoriyanın slaqı')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    def __str__(self):
        return f"{self.name}"

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=60, verbose_name='Teq adı')
    slag = models.SlugField(unique=True, max_length=250, verbose_name='Teqin slaqı')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Teq'
        verbose_name_plural = 'Teq'
        ordering = ['name']


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, related_name='comment_author', verbose_name='İstifadəçi')
    name = models.CharField(max_length=60, verbose_name='Ad')
    email = models.EmailField(verbose_name='E-mail')
    text = models.TextField(verbose_name='Mətn')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post', verbose_name='Xəbər')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Yazılma tarixi')
    published = models.BooleanField(default=True, verbose_name='Aktivlik')

    def __str__(self):
        return f"{self.author}"

    class Meta:
        verbose_name = 'Şərh'
        verbose_name_plural = 'Şərh'
        ordering = ['-create_at']