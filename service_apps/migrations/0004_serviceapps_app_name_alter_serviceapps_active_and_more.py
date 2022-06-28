# Generated by Django 4.0.4 on 2022-06-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_apps', '0003_alter_serviceapps_change_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceapps',
            name='app_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='serviceapps',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='serviceapps',
            name='change_description',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7fd7374bee80>', max_length=150),
        ),
    ]
