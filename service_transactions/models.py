from django.db import models
from service_apps.models import ServiceApp


class Transaction(models.Model):
    class TransactionStatus(models.TextChoices) :
        SUCCESSFUL = 'Successful'
        FAILED = 'Failed'
        PENDING_INTERNAL = 'PendingInternal'
        PENDING_EXTERNAL = 'PendingExternal'
        NA = 'NotAvailable'

    class TransactionType(models.TextChoices):
        AIRTIME = 'AIRTIME'
        SEND_MONEY = 'SEND_MONEY'
        BUY_GOODS = 'BUY_GOODS'
        PAYBILL = 'PAYBILL'


    transaction_id = models.CharField(max_length=50,primary_key=True)
    app_id = models.ForeignKey(ServiceApp, to_field="app_id" , on_delete=models.PROTECT)
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
