# Generated by Django 2.1.7 on 2019-03-20 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0092_auto_20190320_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='nodeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Nodes'),
        ),
    ]
