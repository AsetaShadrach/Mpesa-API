from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ServiceApps(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    app_id = models.CharField(max_length=50, primary_key=True)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    change_description = models.CharField(max_length=150)

    class Meta:
        db_table = 'service_apps'
        verbose_name_plural = 'service_apps'
        ordering = ['-updated_at']

    
    def __str__(self):
        return str(f'''AppID :{self.app_id},
                        CreatedAt : {self.created_at},
                        Creator :{self.creator},
                        Active : {self.active}
                        ''')
        

class Transaction(models.Model):
    class TransactionStatus(models.TextChoices) :
        SUCCESSFUL = 'ST',_('Successful')
        FAILED = 'FT', _('Failed')
        PENDING_INT = 'PTI', _('PendingInternal')
        PENDING_EXT = 'PTE', _('PendingExternal')
        NA = 'NA', _('NotAvailable')

    class TransactionType(models.TextChoices):
        AIRTIME = 'AIRTIME'
        SEND_MONEY = 'SEND_MONEY'
        BUY_GOODS = 'BUY_GOODS'
        PAYBILL = 'PAYBILL'


    transaction_id = models.CharField(max_length=50,primary_key=True)
    app_id = models.ForeignKey(ServiceApps, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=30, choices=TransactionType.choices)
    status = models.CharField(max_length=30, choices= TransactionStatus.choices)
    response_code = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'transactions'
        verbose_name_plural = 'transactions'
        ordering = ['-updated_at']

    def __str__(self):
        return str(f'''TransactionID: {self.transaction_id}, 
                AppID : {self.app_id},
                TransactionDate : {self.created_at},
                TransactionStatus : {self.status},
                ResponseCode : {self.response_code}
                ''')
