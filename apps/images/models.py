from django.db import models
from datetime import datetime


# Create your models here.

class Images(models.Model):

    CATEGORY_TYPE = (
        (100, "班级头像"),
        (101, "班级logo"),
        (200, "活动"),
    )

    image = models.ImageField(upload_to="", verbose_name="图片")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间 ")
    class_id = models.CharField(default="0", max_length=30, verbose_name="班级ID")
    activity_id = models.CharField(default="0", max_length=30, verbose_name="活动ID")
    category = models.IntegerField(choices=CATEGORY_TYPE, default=200, verbose_name="类型")

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


# class Class(models.Model):
#     class Meta:
#         verbose_name = "班级"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
