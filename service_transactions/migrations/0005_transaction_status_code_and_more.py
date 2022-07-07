# Generated by Django 4.0.4 on 2022-07-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_transactions', '0004_transaction_response_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='status_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='response_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]