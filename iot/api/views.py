from django.shortcuts import render
from .models import Nodes,Data,SearchData
from rest_framework import mixins
from .serializers import NodesSerializer,DataSerializer,SearchDataSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import NodesFilter

# Create your views here.
class DataListViewSet(viewsets.ModelViewSet):
    """
    接口允许被查看和修改
    """
    queryset = Data.objects.all().order_by('-recordTime')
    serializer_class = DataSerializer

class SearchDataListViewSet(viewsets.ModelViewSet):
    """
    接口说明
    """
    queryset = Nodes.objects.all().order_by('-keyword')
    serializer_class = SearchDataSerializer

# 可选用的模型mixins.ListModelMixin, viewsets.GenericViewSet 自定义型
class NodesListViewSet(viewsets.ModelViewSet):
    """
    接口说明
    """
    queryset = Nodes.objects.all().order_by('-node_type')
    serializer_class = NodesSerializer
