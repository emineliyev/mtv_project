from django.db import models
from mptt.fields import TreeForeignKey
from mtv import settings
from post.models import Category, Tag


class Slider(models.Model):
    title = models.CharField(max_length=250, verbose_name='Başlıq')
    description = models.TextField(verbose_name='Məzmun')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL,
                               related_name='slider_author', verbose_name='Müəllif')
    image = models.ImageField(upload_to="image/slider/%Y/%m/%d/", null=True, blank=True, verbose_name='Şəkil',
                              help_text='Slayder şəkil ölçüsü 1600X800')
    category = TreeForeignKey(Category, on_delete=models.CASCADE, related_name='slider_category',
                              verbose_name='Kateqoriya')
    tag = models.ManyToManyField(Tag, related_name='slider_tags', verbose_name='Teq')
    view = models.PositiveIntegerField(default=0, verbose_name='Baxış sayı')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Yayım tarixi')
    published = models.BooleanField(default=False, verbose_name='Aktivlik')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Slayder'
        verbose_name_plural = 'Slayder'
        ordering = ['-create_at']
