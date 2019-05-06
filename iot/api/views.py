from django.shortcuts import render
from .models import Nodes,Data,SearchData,Commodity,Order
from rest_framework import mixins,status,filters,viewsets
from .serializers import NodesSerializer,DataSerializer,SearchDataSerializer,OrderSerializer,CommoditySerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import NodesFilter
from .mqtt import *
from rest_framework.decorators import action
from rest_framework.response import Response
from .CountModelMixin import CountModelMixin
from django.db.models import Count,F
from rest_framework.decorators import api_view
from itertools import chain
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
        nodeId = self.request.query_params.get('nodeId', None)
        result = []
        if timescale == 'year':
            queryset = Data.objects.filter(recordTime__year=num)
            if nodeId!='all' and nodeId:
                queryset = queryset.filter(nodeId=nodeId)
            if type == 'count':
                for i in range(1,13):
                    result.insert(i, {'x': str(i)+'月', 'y': len(DataSerializer(queryset.filter(recordTime__month=i), many=True).data)})
            else:
                for i in range(1,13):
                    result.insert(i, {str(i)+'月': DataSerializer(queryset.filter(recordTime__month=i),many=True).data})
        elif timescale == 'month':
            queryset = Data.objects.filter(recordTime__year=2019,recordTime__month=num)
            if nodeId!='all' and nodeId:
                queryset = Data.objects.filter(nodeId=nodeId)
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
        type = self.request.query_params.get('type', None)
        nodeId = self.request.query_params.get('nodeId', None)
        result = []
        if timescale == 'year':
            last_range = datetime.datetime.now() - datetime.timedelta(days=365)
            safeQueryset = Data.objects.filter(recordTime__gte=last_range,safe=True)
            unsafeQueryset = Data.objects.filter(recordTime__gte=last_range,safe=False)
            queryset = Data.objects.filter(recordTime__gte=last_range)
            if nodeId!= 'all' and nodeId:
                safeQueryset=safeQueryset.filter(nodeId=nodeId)
                unsafeQueryset=unsafeQueryset.filter(nodeId=nodeId)
                queryset=queryset.filter(nodeId=nodeId)
            if type == 'count':
                for i in range(1,13):
                    allNum = queryset.filter(recordTime__month=i).count()
                    temp = safeQueryset.filter(recordTime__month=i).count()
                    y=temp/allNum*100 if allNum != 0 else 0
                    result.insert(i,{'x': str(i)+'月','y': y})
            elif type == 'safe':
                for i in range(1,13):
                    result.insert(i, {str(i)+'月': DataSerializer(safeQueryset.filter(recordTime__month=i),many=True).data})
            else:
                for i in range(1,13):
                    result.insert(i, {str(i)+'月': DataSerializer(unsafeQueryset.filter(recordTime__month=i),many=True).data})
        elif timescale == 'month':
            last_range = datetime.datetime.now() - datetime.timedelta(days=31)
            safeQueryset = Data.objects.filter(recordTime__gte=last_range,safe=True)
            unsafeQueryset = Data.objects.filter(recordTime__gte=last_range,safe=False)
            queryset = Data.objects.filter(recordTime__gte=last_range)
            if nodeId!= 'all' and nodeId:
                safeQueryset=safeQueryset.filter(nodeId=nodeId)
                unsafeQueryset=unsafeQueryset.filter(nodeId=nodeId)
                queryset=queryset.filter(nodeId=nodeId)
            if type == 'count':
                for i in range(1,32):
                    allNum = queryset.filter(recordTime__day=i).count()
                    temp = safeQueryset.filter(recordTime__day=i).count()
                    y=temp/allNum*100 if allNum != 0 else 0
                    result.insert(i,{'x': str(i)+'号','y': y})
            elif type == 'safe':
                for i in range(1,32):
                    result.insert(i, {str(i)+'号': DataSerializer(safeQueryset.filter(recordTime__day=i),many=True).data})
            else:
                for i in range(1,32):
                    result.insert(i, {str(i)+'号': DataSerializer(unsafeQueryset.filter(recordTime__day=i),many=True).data})
        elif timescale == 'today':
            last_range = datetime.datetime.now() - datetime.timedelta(days=1)
            safeQueryset = Data.objects.filter(recordTime__gte=last_range,safe=True)
            unsafeQueryset = Data.objects.filter(recordTime__gte=last_range,safe=False)
            queryset = Data.objects.filter(recordTime__gte=last_range)
            if nodeId!= 'all' and nodeId:
                safeQueryset=safeQueryset.filter(nodeId=nodeId)
                unsafeQueryset=unsafeQueryset.filter(nodeId=nodeId)
                queryset=queryset.filter(nodeId=nodeId)
            if type == 'count':
                for i in range(1,25):
                    allNum = queryset.filter(recordTime__hour=i).count()
                    temp = safeQueryset.filter(recordTime__hour=i).count()
                    y=temp/allNum*100 if allNum != 0 else 0
                    result.insert(i,{'x': str(i)+'点','y': y})
            elif type == 'safe':
                for i in range(1,25):
                    result.insert(i, {str(i)+'点': DataSerializer(safeQueryset.filter(recordTime__hour=i),many=True).data})
            else:
                for i in range(1,25):
                    result.insert(i, {str(i)+'点': DataSerializer(unsafeQueryset.filter(recordTime__hour=i),many=True).data})
        return Response(result)

    """
    返回三天的图标，用于linechart表格的展示

    order_by  '-' 从大到小,不加则为从小到大
    """
    @action(detail=False)
    def lineChartData(self, request, *args, **kwargs):
        nodeId = self.request.query_params.get('nodeId', None)
        today_range = datetime.datetime.now() - datetime.timedelta(days=1)
        yesterday_range = datetime.datetime.now() - datetime.timedelta(days=2)
        today_queryset = Data.objects.filter(nodeId=nodeId,recordTime__range=[today_range,datetime.datetime.now()])
        yesterday_queryset = Data.objects.filter(nodeId=nodeId,recordTime__range=[yesterday_range,today_range])
        today_count = today_queryset.count()
        yesterday_count = yesterday_queryset.count()
        today_safe = today_queryset.filter(safe=True).values(x=F('recordTime'),y1=F('val'))
        today_unsafe = today_queryset.filter(safe=False).values(x=F('recordTime'),y2=F('val'))
        yesterday_safe = yesterday_queryset.filter(safe=True).values(x=F('recordTime'),y1=F('val'))
        yesterday_unsafe = yesterday_queryset.filter(safe=False).values(x=F('recordTime'),y2=F('val'))
        result= [{'name':'今天','cvr':today_count},{'name':'昨天','cvr':yesterday_count}]
        for i in today_safe:
            i['y2']=0
        for i in today_unsafe:
            i['y1']=0
        for i in yesterday_safe:
            i['y2']=0
        for i in yesterday_unsafe:
            i['y1']=0
        today = list(chain(today_safe,today_unsafe))
        yesterday = list(chain(yesterday_safe,yesterday_unsafe))
        #today = today_safe | today_unsafe
        #yesterday = yesterday_safe | yesterday_unsafe
        result[0]['shop']=sorted(today, key=lambda x:x['x'])
        result[1]['shop']=sorted(yesterday, key=lambda x:x['x'])
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
        result= round(safeNum/allNum*100,2) if allNum!=0 else 0
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
        count = 0
        if timescale == 'month':
            count = Data.objects.filter(recordTime__year=2019,recordTime__month=num).count()
        elif timescale == 'year':
            count = Data.objects.filter(recordTime__year=num).count()
        elif timescale == 'today':
            last_range = datetime.datetime.now() - datetime.timedelta(days=1)
            count = Data.objects.filter(recordTime__gte=last_range).count()
        elif timescale == 'hour':
            last_range = datetime.datetime.now() - datetime.timedelta(hours=1)
            count = Data.objects.filter(recordTime__gte=last_range).count()
        return Response({'count': count})

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

    """
    返回指定id的所有count数据
    """
    @action(detail=False)
    def getCount(self, request, *args, **kwargs):
        nodeId = self.request.query_params.get('nodeId', None)
        totalCount = Data.objects.filter(nodeId = nodeId).count()
        daily_range = datetime.datetime.now() - datetime.timedelta(days=1)
        dailyCount = Data.objects.filter(nodeId = nodeId, recordTime__gte=daily_range).count()
        return Response({'totalCollect': totalCount,'dailyCollect': dailyCount})

    """
    返回指定id的safe数据
    """
    @action(detail=False)
    def getSafeCount(self, request, *args, **kwargs):
        nodeId = self.request.query_params.get('nodeId', None)
        totalCount = Data.objects.filter(nodeId=nodeId).count()
        totalSafeCount = Data.objects.filter(nodeId=nodeId, safe=True).count()
        daily_range = datetime.datetime.now() - datetime.timedelta(days=1)
        dailySafeCount = Data.objects.filter(nodeId=nodeId, recordTime__gte=daily_range).count()
        totalSafe = round(totalSafeCount / totalCount *100,2) if totalCount!= 0 else 0
        dailySafe = round(dailySafeCount / totalCount *100,2) if totalCount!=0 else 0
        return Response({'totalSafe': totalSafe,'dailySafe': dailySafe})

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
    search_fields = ('keyword', 'count', 'status')
    filter_fields = ('keyword', 'count', 'status')

    @action(detail=False,methods=['POST'])
    def addHistory(self, request, *args, **kwargs):
        searchName = self.request.data.get('keyword')
        try:
            searchHistory = SearchData.objects.filter(keyword=searchName)
            if searchHistory.count() > 0:
                count = SearchData.objects.get(keyword=searchName).count + 1
                searchHistory.update(count=count)
                return Response({'msg:':'add history count successfully'},status=status.HTTP_200_OK)
            else:
                searchHistory = SearchData(keyword=searchName)
                searchHistory.save()
                return Response({'msg': 'add history data successfully'},status= status.HTTP_200_OK)
        except:
            searchHistory = SearchData(keyword=searchName)
            searchHistory.save()
            return Response({'msg': searchHistory},status= status.HTTP_200_OK)

 #           return Response({'msg':'error'},status= status.HTTP_400_BAD_REQUEST)

# 可选用的模型mixins.ListModelMixin, viewsets.GenericViewSet 自定义型
class NodesListViewSet(viewsets.ModelViewSet, CountModelMixin):
    """
    接口说明
    """
    queryset = Nodes.objects.all().order_by('-node_type')
    serializer_class = NodesSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('node_name', 'node_type', 'minVal', 'maxVal', 'adcode','nodeId','subscribe')
    filter_fields = ('node_name', 'node_type', 'minVal', 'maxVal', 'adcode','nodeId','subscribe')

    @action(detail=True,methods=['POST'])
    def subscribe(self,request,*args,**kwargs):
        nodeId = self.request.data.get('nodeId')
        subscribe =self.request.data.get('subscribe')
        try:
            subscribeNode =Nodes.objects.get(nodeId=nodeId)
            subscribeNode.subscribe=subscribe
            subscribeNode.save()
            #mqtt.client.loop_start()
            return Response({'msg':'successfully change'},status=status.HTTP_200_OK)
        except:
            return Response({'msg':'error with nodeId'},status=status.HTTP_404_NOT_FOUND)
