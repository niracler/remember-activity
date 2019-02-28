from django.db import models
from datetime import datetime


# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to="", verbose_name="图片")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间 ")

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)
