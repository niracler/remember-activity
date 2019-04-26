import django_filters
from .models import Images


class ImagesFiliter(django_filters.rest_framework.FilterSet):
    """图片的过滤类"""

    class_id = django_filters.CharFilter(field_name='class_id')
    activity_id = django_filters.CharFilter(field_name='activity_id')
    category = django_filters.NumberFilter(field_name='category')

    class Meta:
        model = Images
        fields = ['class_id', 'activity_id', 'category']