# Generated by Django 2.1.7 on 2019-05-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('send_time', models.DateTimeField(auto_now=True, verbose_name='发送时间')),
                ('code', models.CharField(default='', max_length=10, verbose_name='验证码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('send_type', models.CharField(default='', max_length=15, verbose_name='请求类型')),
            ],
            options={
                'verbose_name': '验证码',
                'verbose_name_plural': '验证码',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('currentAuthority', models.CharField(default='user', max_length=10)),
                ('nickname', models.CharField(default='', max_length=20)),
                ('summary', models.CharField(default='', max_length=256)),
                ('adcode', models.CharField(default='', max_length=15)),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
        ),
    ]
