# Generated by Django 2.1.7 on 2019-04-03 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0242_auto_20190403_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='nodeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Nodes'),
        ),
    ]
