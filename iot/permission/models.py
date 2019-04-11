from django.db import models

# Create your models here.
class User(models.Model):
    """
    个人信息
    account password
    email nickname
    summary
    adcode
    address
    phone
    """
    id = models.AutoField(primary_key=True)
    #account = models.CharField(max_length=128, unique=True,)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=20,default='')
    summary = models.CharField(max_length=256,default='')
    adcode = models.CharField(max_length=15,default='')
    address = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=20,default='')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.id + ' s mail:' + self.email


