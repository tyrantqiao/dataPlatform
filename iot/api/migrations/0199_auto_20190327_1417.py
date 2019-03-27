# Generated by Django 2.1.7 on 2019-03-27 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0198_auto_20190326_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodes',
            name='adcode',
            field=models.CharField(default=440100, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nodes',
            name='latitude',
            field=models.FloatField(default=23.13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nodes',
            name='longitude',
            field=models.FloatField(default=113.27),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='nodeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Nodes'),
        ),
    ]
