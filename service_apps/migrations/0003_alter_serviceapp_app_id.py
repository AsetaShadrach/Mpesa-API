# Generated by Django 4.0.4 on 2022-07-01 12:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('service_apps', '0002_alter_serviceapp_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceapp',
            name='app_id',
            field=models.UUIDField(default=uuid.UUID('ca48f7a9-2f00-4862-969b-a18f5d1afbdf'), primary_key=True, serialize=False),
        ),
    ]
