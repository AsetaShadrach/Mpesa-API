from django.contrib import admin
from .models import Transaction, ServiceApps

admin.site.register([Transaction,ServiceApps])
