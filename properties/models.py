from django.db import models


class Contacts(models.Model):
    phone = models.CharField(max_length=60, blank=True, null=True,  verbose_name='Telefon')
    address = models.CharField(max_length=250, blank=True, null=True,  verbose_name='Ünvan')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    soc_link_1 = models.URLField(blank=True, null=True, verbose_name='Sosial link 1')
    soc_icon_1 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Sosial ikon 1', help_text=(
        'fa-facebook',
        'fa-instagram',
        'fa-linkedin',
        'fa-twitter',
        'fa-vk'
    ))
    soc_link_2 = models.URLField(blank=True, null=True, verbose_name='Sosial link 2')
    soc_icon_2 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Sosial ikon 2', help_text=(
        'fa-facebook',
        'fa-instagram',
        'fa-linkedin',
        'fa-twitter',
        'fa-vk'
    ))
    soc_link_3 = models.URLField(blank=True, null=True, verbose_name='Sosial link 3')
    soc_icon_3 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Sosial ikon 3', help_text=(
        'fa-facebook',
        'fa-instagram',
        'fa-linkedin',
        'fa-twitter',
        'fa-vk'
    ))
    soc_link_4 = models.URLField(blank=True, null=True, verbose_name='Sosial link 4')
    soc_icon_4 = models.CharField(max_length=60, blank=True, null=True, verbose_name='Sosial ikon 4', help_text=(
        'fa-facebook',
        'fa-instagram',
        'fa-linkedin',
        'fa-twitter',
        'fa-vk'
    ))

    def __str__(self):
        return f"Əlaqə"

    class Meta:
        verbose_name = 'Əlaqə'
        verbose_name_plural = 'Əlaqə'


class Logo(models.Model):
    image = models.ImageField(upload_to="image/logo/%Y/%m/%d/")

    def __str__(self):
        return f"Logo"

    class Meta:
        verbose_name = 'Loqotip'
        verbose_name_plural = 'Loqotip'


class Advertising(models.Model):
    customer = models.CharField(max_length=250, verbose_name='Sifarişçi')
    customer_url = models.URLField(verbose_name='link', blank=True, null=True)
    image = models.ImageField(upload_to="image/advertising/%Y/%m/%d/", verbose_name='Şəkil', help_text='Şəkil ölçüsü 400X500')
    published = models.BooleanField(default=False, verbose_name='Aktivlik')
    create_at = models.DateField(auto_now_add=True, verbose_name='Yayım tarixi')

    def __str__(self):
        return f"{self.customer}"

    class Meta:
        verbose_name = 'Reklam'
        verbose_name_plural = 'Reklam'
        ordering = ['-create_at']
