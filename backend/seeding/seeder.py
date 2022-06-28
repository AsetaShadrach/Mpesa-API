from distutils.command.config import config
from django_seed import Seed
from service_transactions.models import Transaction
from service_apps.models import ServiceApps
from django.contrib.auth.models import User
from decouple import config
import uuid
import random


class SeedData():
    def __init__(self, app_number, total_transactions) -> None:
        self.app_number = app_number
        self.total_transactions = total_transactions


    def create_apps(self):
        user  =  User.objects.all().first()
        for i in range(0,self.app_number):
            app = ServiceApps( creator = str(user.username),
                        app_id = uuid.uuid4(),
                        app_name = "app" + str(i+1),
                        active = False,
                        tr_count_l_d = random.randint(10, 1000),
                        tr_count_l_7d = random.randint(1000, 10000),
                        tr_count_l_30d = random.randint(1000, 100000),
                        tr_cum_sum_l_d = random.randint(1000000, 10000000)/10.0 ,
                        tr_cum_sum_l_7d = random.randint(10000000, 100000000)/10.0 ,
                        tr_cum_sum_l_30d = random.randint(10000000, 1000000000)/10.0 ,
                        change_description = "Updated by " + str(user.username)
                        )
            app.save()
    
    def create_transactions(self):
        tr_types = list(Transaction.TransactionType)
        tr_status = list(Transaction.TransactionStatus)
        for _ in range(0,self.total_transactions):
            Transaction (
                transaction_id = uuid.uuid4(),
                app_id = ServiceApps.objects.order_by('?').first(),
                transaction_type = random.choice(tr_types),
                status = random.choice(tr_status),
                response_code = 200,
            ).save()
            
        