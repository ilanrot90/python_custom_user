from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, max_length=48, help_text='Contact phone number')
    country = CountryField(blank=True, null=True, blank_label='(select country)')

    def __str__(self):
        return self.email
