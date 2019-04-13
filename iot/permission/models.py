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
    currentAuthority =  models.CharField(max_length=10,default='user')
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

class EmailCode(models.Model):
    id = models.AutoField(primary_key=True)
    send_time = models.DateTimeField('发送时间', auto_now = True)
    code = models.CharField('验证码', max_length=10, default='')
    email = models.EmailField('邮箱')
    send_type = models.CharField('请求类型',max_length=15, default='')

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email +' code:' + self.code
