# Generated by Django 2.1.7 on 2019-05-07 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190507_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='nodeId',
            field=models.ForeignKey(blank=True, db_column='nodeId', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Nodes', to_field='nodeId'),
        ),
    ]
