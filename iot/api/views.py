from django.shortcuts import render
from .models import Nodes
from rest_framework import mixins
from .serializers import NodesSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import NodesFilter

# Create your views here.
class NodesPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = "page"
    # 默认值
    page_size = 2
    max_page_size = 100

class NodesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    """
    接口说明
    """
    queryset = Nodes.objects.all()
    serializer_class = NodesSerializer
    pagination_class = NodesPagination
    # 自定义过滤（没有下面会报错）
    filter_class = NodesFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 搜索
    search_fields = ('id','name','type','safe')
