# Generated by Django 4.0.6 on 2022-07-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ad')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Soyad')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/author/%Y/%m/%d/', verbose_name='Şəkil')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefon')),
            ],
            options={
                'verbose_name': 'İstifadəçi',
                'verbose_name_plural': 'İstifadəçilər',
            },
        ),
    ]
