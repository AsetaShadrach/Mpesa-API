# Generated by Django 4.0.4 on 2022-06-24 16:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Application',
            new_name='ServiceApps',
        ),
        migrations.AlterModelOptions(
            name='serviceapps',
            options={'ordering': ['-updated_at'], 'verbose_name_plural': 'service_apps'},
        ),
        migrations.AlterModelTable(
            name='serviceapps',
            table='service_apps',
        ),
    ]