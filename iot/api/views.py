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
from django.db.models import Count
import datetime

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

    """
    根据时间返回list数据
    """
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

    """
    根据时间尺度分割，并返回相应的数据，其中type有2种类型，默认为data，然后就是count
    """
    @action(detail=False)
    def segmentData(self, request, *args, **kwargs):
        timescale = self.request.query_params.get('timescale', None)
        num = self.request.query_params.get('num', None)
        type = self.request.query_params.get('type', None)
        result = []
        if timescale == 'year':
            queryset = Data.objects.filter(recordTime__year=num)
            if type == 'count':
                for i in range(1,13):
                    result.insert(i, {'x': str(i)+'月', 'y': len(DataSerializer(queryset.filter(recordTime__month=i), many=True).data)})
            else:
                for i in range(1,13):
                    result.insert(i, {str(i)+'月': DataSerializer(queryset.filter(recordTime__month=i),many=True).data})
        elif timescale == 'month':
            queryset = Data.objects.filter(recordTime__year=2019,recordTime__month=num)
            if type == 'count':
                for i in range(1,32):
                    result.insert(i, {'x': str(i)+'号', 'y': len(DataSerializer(queryset.filter(recordTime__day=i), many=True).data)})
            else:
                for i in range(1,32):
                    result.insert(i, {str(i)+'号': DataSerializer(queryset.filter(recordTime__day=i),many=True).data})
        return Response(result)

    """
    根据时间尺度返回安全率数值   type有三个值  count、safe、unsafe
    """
    @action(detail=False)
    def segmentSafe(self, request, *args, **kwargs):
        timescale = self.request.query_params.get('timescale', None)
        num = self.request.query_params.get('num', None)
        type = self.request.query_params.get('type', None)
        result = []
        if timescale == 'year':
            safeQueryset = Data.objects.filter(recordTime__year=num,safe=True)
            unsafeQueryset = Data.objects.filter(recordTime__year=num,safe=False)
            queryset = Data.objects.filter(recordTime__year=num)
            if type == 'count':
                for i in range(1,13):
                    allNum = len(DataSerializer(queryset.filter(recordTime__month=i),many=True).data)
                    temp = len(DataSerializer(safeQueryset.filter(recordTime__month=i), many=True).data)
                    y=temp/allNum*100 if allNum != 0 else 0
                    result.insert(i,{'x': str(i)+'月','y': y})
            elif type == 'safe':
                for i in range(1,13):
                    result.insert(i, {str(i)+'月': DataSerializer(safeQueryset.filter(recordTime__month=i),many=True).data})
            else:
                for i in range(1,13):
                    result.insert(i, {str(i)+'月': DataSerializer(unsafeQueryset.filter(recordTime__month=i),many=True).data})
        elif timescale == 'month':
            safeQueryset = Data.objects.filter(recordTime__year=2019,recordTime__month=num,safe=True)
            unsafeQueryset = Data.objects.filter(recordTime__year=2019,recordTime__month=num,safe=False)
            queryset = Data.objects.filter(recordTime__year=2019,recordTime__month=num)
            if type == 'count':
                for i in range(1,32):
                    allNum = len(DataSerializer(queryset.filter(recordTime__day=i),many=True).data)
                    temp = len(DataSerializer(safeQueryset.filter(recordTime__day=i), many=True).data)
                    y=temp/allNum*100 if allNum != 0 else 0
                    result.insert(i,{'x': str(i)+'号','y': y})
            elif type == 'safe':
                for i in range(1,32):
                    result.insert(i, {str(i)+'号': DataSerializer(safeQueryset.filter(recordTime__day=i),many=True).data})
            else:
                for i in range(1,32):
                    result.insert(i, {str(i)+'号': DataSerializer(unsafeQueryset.filter(recordTime__day=i),many=True).data})
        return Response(result)

    @action(detail=False)
    def realTimeSafe(self, request, *args, **kwargs):
        """实时安全率

        根据时间尺度返回实时安全率数据
        gte greater      lt  less then

        Args:
            timescale: 时间尺度,可为hour,day,week,month,year

        Returns:
            返回实时安全率数值，以dict的形式

            {'safeRate': 15}
        """
        timescale = self.request.query_params.get('timescale',None)
        last_range = ''
        if timescale == 'hour':
            last_range = datetime.datetime.now() - datetime.timedelta(hours=1)
        elif timescale == 'day':
            last_range = datetime.datetime.now() - datetime.timedelta(days=1)
        elif timescale == 'week':
            last_range = datetime.datetime.now() - datetime.timedelta(weeks=7)
        elif timescale == 'month':
            last_range = datetime.datetime.now() - datetime.timedelta(days=30)
        else:
            last_range = datetime.datetime.now() -datetime.timedelta(days=365)
        safeNum = Data.objects.filter(recordTime__gte=last_range,safe=True).count()
        allNum = Data.objects.filter(recordTime__gte=last_range).count()
        result= safeNum/allNum*100 if allNum!=0 else 0

        return Response({'safeRate': result})

    @action(detail=False)
    def countByTimescale(self, request, *args, **kwargs):
        """根据时间返回count值

        timescale可为年月类型，然后根据查询的时间数字，返回需要的count数据

        Args:
            timescale: 时间尺度可为年月
            num: 查询时间

        Returns:
            返回一个dict类型，count数值
            示例：

            {'count': 12}
        """
        timescale = self.request.query_params.get('timescale', None)
        num = self.request.query_params.get('num', None)
        if timescale == 'month':
            queryset = Data.objects.filter(recordTime__year=2019,recordTime__month=num)
        elif timescale == 'year':
            queryset = Data.objects.filter(recordTime__year=num)
        serializer = DataSerializer(queryset, many=True)
        return Response({'count': len(serializer.data)})

    """
    返回数据收集排名榜，做个名字加数字总和
    """
    @action(detail=False)
    def countRank(self, request, *args, **kwargs):
        limit = self.request.query_params.get('limit', None)
        type = self.request.query_params.get('type', None)
        result= []
        if type == 'data':
            queryset = Nodes.objects.annotate(num=Count('data__nodeId')).order_by('-num')[:int(limit)]
            for i in queryset:
                result.append({'title': i.node_name,'total': i.num})
        elif type == 'safe':
            queryset = Nodes.objects.annotate(num=Count('data__nodeId')).order_by('-num')[:int(limit)]
            safeQueryset = Nodes.objects.filter(data__safe=True).annotate(num=Count('data__nodeId')).order_by('-num')[:int(limit)]
            for i in range(len(safeQueryset)):
                safeRate=safeQueryset[i].num/queryset[i].num*100 if queryset[i].num!=0 else 0
                result.append({'title': queryset[i].node_name,'total': safeRate})
        return Response(result)

class OrderListViewSet(viewsets.ModelViewSet, CountModelMixin):
    """
    接口说明
    """
    queryset = Order.objects.all().order_by('-amount')
    serializer_class = OrderSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'commodityId', 'amount')
    filter_fields = ('id', 'commodityId', 'amount')

class CommodityListViewSet(viewsets.ModelViewSet, CountModelMixin):
    """
    接口说明
    """
    queryset = Commodity.objects.all().order_by('-y')
    serializer_class = CommoditySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'x', 'type','y')
    filter_fields = ('id', 'x', 'type','y')


    @action(detail=False)
    def getSalesTypeData(self, request, *args, **kwargs):
        queryset = Commodity.objects.values('x','y','type')
        return Response(queryset)

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
