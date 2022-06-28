# Generated by Django 4.0.4 on 2022-06-28 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceApps',
            fields=[
                ('app_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('active', models.BooleanField()),
                ('service_details', models.JSONField(default=dict)),
                ('tr_count_l_d', models.IntegerField(default=0)),
                ('tr_count_l_7d', models.IntegerField(default=0)),
                ('tr_count_l_30d', models.IntegerField(default=0)),
                ('tr_cum_sum_l_d', models.FloatField(default=0)),
                ('tr_cum_sum_l_7d', models.FloatField(default=0)),
                ('tr_cum_sum_l_30d', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('change_description', models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f530c33beb0>', max_length=150)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'service_apps',
                'db_table': 'service_apps',
                'ordering': ['-created_at'],
            },
        ),
    ]
