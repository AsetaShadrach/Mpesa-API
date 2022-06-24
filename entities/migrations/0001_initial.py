# Generated by Django 4.0.4 on 2022-06-24 16:47

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
            name='Application',
            fields=[
                ('app_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('active', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('change_description', models.CharField(max_length=150)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'applications',
                'db_table': 'applications',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('AIRTIME', 'Airtime'), ('SEND_MONEY', 'Send Money'), ('BUY_GOODS', 'Buy Goods'), ('PAYBILL', 'Paybill')], max_length=30)),
                ('status', models.CharField(choices=[('ST', 'Successful'), ('FT', 'Failed'), ('PTI', 'PendingInternal'), ('PTE', 'PendingExternal'), ('NA', 'NotAvailable')], max_length=30)),
                ('response_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entities.application')),
            ],
            options={
                'verbose_name_plural': 'transactions',
                'db_table': 'transactions',
                'ordering': ['-updated_at'],
            },
        ),
    ]
