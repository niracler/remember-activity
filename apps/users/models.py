from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    """API后台用户"""

    name = models.CharField(max_length=30, null=True, verbose_name="姓名")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="电子邮件")

    class Meta:
        verbose_name = "API后台用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
