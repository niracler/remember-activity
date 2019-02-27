from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins, viewsets
from .models import Images
from .serializer import ImagesSerializer


# Create your views here.

class ImagesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ImagesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """图片的列表API"""
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    pagination_class = ImagesPagination
