# Generated by Django 2.1.7 on 2019-05-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nodes',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
