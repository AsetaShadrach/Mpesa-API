# Generated by Django 4.0.4 on 2022-06-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Successful', 'Successful'), ('Failed', 'Failed'), ('PendingInternal', 'Pending Internal'), ('PendingExternal', 'Pending External'), ('NotAvailable', 'Na')], max_length=30),
        ),
    ]
