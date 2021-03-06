from django.db import models
from django.contrib.auth import models as mod
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, password, **other_fields)

    def create_user(self, email, first_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUserModel(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=False, null=True)
    first_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]

    def __str__(self):
        return self.email


class Advisor(models.Model):
    advisor_name = models.CharField(max_length=50)
    advisor_pic = models.ImageField(upload_to='advisorPics/')

class Booking(models.Model):
    booking_time = models.DateTimeField(auto_now_add=False)
    advisor_booked = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    by_user = models.ForeignKey(NewUserModel, on_delete=models.CASCADE)
