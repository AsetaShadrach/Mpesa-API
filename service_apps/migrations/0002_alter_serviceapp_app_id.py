# Generated by Django 4.0.4 on 2022-07-01 12:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('service_apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceapp',
            name='app_id',
            field=models.UUIDField(default=uuid.UUID('81786f87-895b-4a20-ace1-974fc0e1ac51'), primary_key=True, serialize=False),
        ),
    ]
