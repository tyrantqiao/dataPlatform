# Generated by Django 2.1.7 on 2019-03-22 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0135_auto_20190322_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='nodeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Nodes'),
        ),
    ]
