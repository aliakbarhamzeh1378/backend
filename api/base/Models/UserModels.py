from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from api.base.managers import userModelManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(_('email address'), null=False, unique=True)
    phone = PhoneNumberField(blank=False, null=False, unique=True, region="IR")
    first_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    objects = userModelManager()

    def __str__(self):
        return self.email
