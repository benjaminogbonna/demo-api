from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), max_length=150, unique=True)
    name = models.CharField(_("name"), max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(verbose_name="Phone", max_length=20, default='', null=True, blank=True)
    address = models.CharField(verbose_name="Address", max_length=100, default='', null=True, blank=True)
    city = models.CharField(verbose_name="Town/City", max_length=100, default='', null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=100, default='', null=True, blank=True)
    agreed_to_terms_and_p_policy = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'agreed_to_terms_and_p_policy']

    objects = CustomUserManager()

    class Meta:
        ordering = ('-date_joined',)

    def __str__(self):
        return self.username
