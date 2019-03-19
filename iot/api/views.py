from django.shortcuts import render
from .models import Nodes,Data,SearchData,Commodity,Order
from rest_framework import mixins
from .serializers import NodesSerializer,DataSerializer,SearchDataSerializer,OrderSerializer,CommoditySerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import NodesFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from .CountModelMixin import CountModelMixin
from rest_framework.response import Response

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
    
    """
    根据时间段返回list数据
    """
    @action(detail=False)
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date or end_date:
            queryset = queryset.filter(recordTime__range=[start_date, end_date])
            serializer = DataSerializer(queryset, many=True)
            return Response(serializer.data)
    
    @action(detail=False)
    def getByTimescale(self, request, *args, **kwargs):
        timescale = self.request.query_params.get('timescale', None)
        num = self.request.query_params.get('num', None)
        if timescale == 'month':
            queryset = Data.objects.filter(recordTime__month=num)
        elif timescale == 'year':
            queryset = Data.objects.filter(recordTime__year=num)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def segmentByTimescale(self, request, *args, **kwargs):
        timescale = self.request.query_params.get('timescale', None)
        num = self.request.query_params.get('num', None)
        result = []
        if timescale == 'Year':
            queryset = Data.objects.filter(recordTime__year=num)
            for i in range(12):
                result.insert({i: queryset.filter(recordTime__month=i)})
        return Response(result)

    @action(detail=False)
    def countByTimescale(self, request, *args, **kwargs):
        timescale = self.request.query_params.get('timescale', None)
        num = self.request.query_params.get('num', None)
        if timescale == 'month':
            queryset = Data.objects.filter(recordTime__month=num)
        elif timescale == 'year':
            queryset = Data.objects.filter(recordTime__year=num)
        serializer = DataSerializer(queryset, many=True)
        return Response({'count': len(serializer.data)})

class OrderListViewSet(viewsets.ModelViewSet, CountModelMixin):
    """
    接口说明
    """
    queryset = SearchData.objects.all().order_by('-amount')
    serializer_class = OrderSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)    
    search_fields = ('id', 'commodityId', 'amount')
    filter_fields = ('id', 'commodityId', 'amount')

    @action(detail=False)
    def addOrder(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                

        
class CommodityListViewSet(viewsets.ModelViewSet, CountModelMixin):
    """
    接口说明
    """
    queryset = Commodity.objects.all().order_by('-sales')
    serializer_class = CommoditySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)    
    search_fields = ('id', 'name', 'location', 'type','sales')
    filter_fields = ('id', 'name', 'location', 'type','sales')

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
