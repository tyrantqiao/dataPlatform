from django.db import models

# Create your models here.
class Nodes(models.Model):
    """数据节点模型页

    用于管理数据节点，同时也是数据模型的关联项

    Attributes:
        id: index,primary_key
        node_name: 数据节点名字
        node_type: 数据节点类型
        minVal: 最小工作值
        maxVal: 最大工作值
    """
    id = models.AutoField(primary_key=True)
    node_name = models.CharField(max_length=20)
    node_type = models.CharField(max_length=20)
    minVal = models.IntegerField()
    maxVal = models.IntegerField()

    class Meta:
        verbose_name = "数据节点"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.node_name + str(self.id)

# 搜索数据
class SearchData(models.Model):
    """搜索历史模型页

    用于搜索历史的记录

    Attributes:
        id: index
        keyword: 关键词
        count: 排名
        range: 涨幅
        status: 状态
    """
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=20)
    count = models.IntegerField()
    range = models.FloatField()
    status = models.FloatField()

    class Meta:
        verbose_name = "搜索数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)+ ':' + self.keyword

# 商品
class Commodity(models.Model):
    """商品页

    用于做农贸商品的记录，与订单表联动

    Attributes:
        id: index
        x: 商品名字，这里直接作为表格的x轴
        y: 商品总成交额，作为y轴
        type: 商品的销售平台类型，电商门店其他
    """
    id = models.AutoField(primary_key=True)
    x = models.CharField(max_length=25)
    type = models.IntegerField()
    y = models.FloatField()

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id) + ':' + self.x + ': ' + str(self.type) + ':' + str(self.y)


# 订单
class Order(models.Model):
    """订单模型页

    与商品页联动

    Attributes:
        id: index
        commodityId: 商品id
        amount: 订单额
    """
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id) + ':' + self.commodityId + ':' + str(self.amount)

# 数据节点收集数据
class Data(models.Model):
    """data页

    与数据节点页联动

    Attributes:
        id: index
        nodeId: 数据节点id
        val: 数值
        unit: 单位
        safe: 数据是否安全
        recordTime: 数据记录时间
    """
    id = models.AutoField(primary_key=True)
    nodeId = models.ForeignKey(Nodes, on_delete=models.CASCADE)
    val = models.FloatField()
    unit = models.CharField(max_length=10)
    safe = models.BooleanField()
    recordTime = models.DateTimeField()

    class Meta:
        verbose_name = "数值表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.nodeId) + ':' + str(self.val) + self.unit + ',date:' + str(self.recordTime)
