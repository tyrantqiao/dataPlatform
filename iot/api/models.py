from django.db import models

# Create your models here.
class Nodes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    max_val = models.IntegerField()
    min_val = models.IntegerField()
    
    class Meta:
        verbose_name = "数据节点"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + self.id

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.ForeignKey(Nodes, on_delete=models.CASCADE)
    val = models.IntegerField()
    unit = models.CharField(max_length=10)
    safe = models.BooleanField()
    record_time = models.DateField()

    class Meta:
        verbose_name = "数值表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.node_id + ':' + self.val + self.unit + ',date:' + self.record_time
