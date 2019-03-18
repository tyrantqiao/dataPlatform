from django.shortcuts import render
from .models import Nodes,Data,SearchData
from rest_framework import mixins
from .serializers import NodesSerializer,DataSerializer,SearchDataSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import NodesFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from .CountModelMixin import CountModelMixin

# Create your views here.
class DataListViewSet(viewsets.ModelViewSet, CountModelMixin):
    """
    接口允许被查看和修改
    """
    queryset = Data.objects.all().order_by('-recordTime')
    serializer_class = DataSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('nodeId', 'recordTime', 'val', 'safe', 'unit')
    filter_fields = ('nodeId', 'recordTime', 'val', 'safe', 'unit')

class SearchDataListViewSet(viewsets.ModelViewSet, CountModelMixin):
    """
    接口说明
    """
    queryset = SearchData.objects.all().order_by('-keyword')
    serializer_class = SearchDataSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)    
    search_fields = ('keyword', 'count', 'range', 'status')
    filter_fields = ('keyword', 'count', 'range', 'status')

# 可选用的模型mixins.ListModelMixin, viewsets.GenericViewSet 自定义型
class NodesListViewSet(viewsets.ModelViewSet, CountModelMixin):
    """
    接口说明
    """
    queryset = Nodes.objects.all().order_by('-node_type')
    serializer_class = NodesSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('node_name', 'node_type', 'minVal', 'maxVal')
    filter_fields = ('node_name', 'node_type', 'minVal', 'maxVal')
