# Generated by Django 2.1.7 on 2019-03-06 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190306_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='node_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Nodes'),
        ),
    ]
