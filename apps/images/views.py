# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from datetime import datetime
from .filiters import ImagesFiliter
from .models import Images
from .serializer import ImagesSerializer, ImagesCreateSerializer


# Create your views here.

class ImagesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ImagesViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """图片的列表API"""
    queryset = Images.objects.all()
    # serializer_class = ImagesSerializer  # 序列化函数
    pagination_class = ImagesPagination  # 分页函数
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ImagesFiliter
    search_fields = ('id', 'class_id')  # 搜索
    ordering_fields = ('add_time', 'id', 'class_id')  # 排序

    def get_serializer_class(self):
        if self.action == "list":
            return ImagesSerializer
        elif self.action == "create":
            return ImagesCreateSerializer
        return ImagesSerializer