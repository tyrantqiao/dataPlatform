# Generated by Django 2.1.7 on 2019-05-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190506_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='reference',
            field=models.CharField(default='', max_length=100),
        ),
    ]
