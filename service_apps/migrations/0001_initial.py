# Generated by Django 4.0.4 on 2022-06-30 11:10

import collections
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceApp',
            fields=[
                ('creator', models.CharField(default='Not Given', max_length=50)),
                ('app_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('app_name', models.CharField(max_length=50, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('tr_count_l_d', models.IntegerField(default=0)),
                ('tr_count_l_7d', models.IntegerField(default=0)),
                ('tr_count_l_30d', models.IntegerField(default=0)),
                ('tr_cum_sum_l_d', models.FloatField(default=0)),
                ('tr_cum_sum_l_7d', models.FloatField(default=0)),
                ('tr_cum_sum_l_30d', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service_details', models.JSONField(default=collections.OrderedDict)),
            ],
            options={
                'verbose_name_plural': 'service_apps',
                'db_table': 'service_apps',
                'ordering': ['-created_at'],
            },
        ),
    ]
