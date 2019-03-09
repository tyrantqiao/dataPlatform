from django.db import models

# Create your models here.
class Nodes(models.Model):
    id = models.AutoField(primary_key=True)
    nodeName = models.CharField(max_length=20)
    nodeType = models.CharField(max_length=20)
    maxVal = models.IntegerField()
    minVal = models.IntegerField()
    
    class Meta:
        verbose_name = "数据节点"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nodeName + self.id

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
        return self.nodeId + ':' + self.val + self.unit + ',date:' + self.recordTime
