from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    service = models.CharField(blank=True, max_length=100, null=True)
    user_type = models.CharField(blank=True, max_length=50, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email

#TestResult Table
class TestResult(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	reult = models.CharField(_('result'), max_length=50, null=True)