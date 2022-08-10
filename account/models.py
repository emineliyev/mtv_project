from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, verbose_name='Ad', blank=True, null=True)
    last_name = models.CharField(max_length=100, verbose_name='Soyad', blank=True, null=True)
    photo = models.ImageField(upload_to="image/author/%Y/%m/%d/", verbose_name='Şəkil', blank=True, null=True)
    phone = models.CharField(max_length=30, verbose_name='Telefon', blank=True, null=True)

    class Meta:
        verbose_name = 'İstifadəçi'
        verbose_name_plural = 'İstifadəçilər'

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin