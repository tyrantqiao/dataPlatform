# Generated by Django 2.1.7 on 2019-05-06 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190505_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='intensity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='time',
            field=models.CharField(default='', max_length=50),
        ),
    ]
