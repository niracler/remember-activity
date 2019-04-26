from rest_framework import serializers
from .models import Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class ImagesCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True, label="图片")
    class_id = serializers.CharField(required=True, label="班级ID")
    activity_id = serializers.CharField(required=True, label="活动ID")
    category = serializers.IntegerField(required=True, label="类型")

    class Meta:
        model = Images
        fields = ('image', 'class_id', 'activity_id', 'category')
