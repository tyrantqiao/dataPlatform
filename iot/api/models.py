from django.db import models

# Create your models here.
class Nodes(models.Model):
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

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    nodeId = models.ForeignKey(Nodes, on_delete=models.CASCADE)
    val = models.IntegerField()
    unit = models.CharField(max_length=10)
    safe = models.BooleanField()
    recordTime = models.DateTimeField()

    class Meta:
        verbose_name = "数值表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.nodeId) + ':' + str(self.val) + self.unit + ',date:' + self.recordTime
