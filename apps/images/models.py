from django.db import models
from datetime import datetime


# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=300, verbose_name="图片名")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name="图片url")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间 ")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
