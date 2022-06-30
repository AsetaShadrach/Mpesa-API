from service_transactions.models import Transaction
from service_apps.models import ServiceApp
from django.contrib.auth.models import User
from decouple import config
import uuid
import random
from collections import OrderedDict
import json
import calendar

class HistoryDict(OrderedDict):
    def __missing__(self, key):
        val = self[key] = HistoryDict()
        return val

class SeedData():
    def __init__(self, app_number, total_transactions) -> None:
        self.app_number = app_number
        self.total_transactions = total_transactions
    
    def create_user(self):
        User(username='testuser', email='testuser@outlook.com', password='').save()

    def create_dummy_details(self):
        months = [calendar.month_name[i].lower() for i in range(1,13)]
        years = ['2020','2021']

        summary_dict = {
                    'total': (27158, 1316152),
                    'airtime_total': (1234,373740),
                    'buygoods_total' : (1234,292220),
                    'sendmoney_total': (12345,293830),
                    'paybill_total': (12345,356362),
                    }

        service_history = HistoryDict()

        for year in years:
            for month in months:
                service_history[year][month] = summary_dict 
        
        self.APP_METADATA = json.loads(json.dumps(service_history))


    def create_apps(self):
        user  =  User.objects.all().first()
        app_count = ServiceApp.objects.all().count()
        self.create_dummy_details()
        for i in range(0,self.app_number):
            app = ServiceApp( creator = str(user.username),
                        app_id = uuid.uuid4(),
                        app_name = "app" + str(i+app_count+1),
                        active = False,
                        tr_count_l_d = random.randint(10, 1000),
                        tr_count_l_7d = random.randint(1000, 10000),
                        tr_count_l_30d = random.randint(1000, 100000),
                        tr_cum_sum_l_d = random.randint(1000000, 10000000),
                        tr_cum_sum_l_7d = random.randint(10000000, 100000000),
                        tr_cum_sum_l_30d = random.randint(10000000, 1000000000),
                        service_details = self.APP_METADATA
                        )
            app.save()
    
    def create_transactions(self):
        tr_types = list(Transaction.TransactionType)
        tr_status = list(Transaction.TransactionStatus)
        for _ in range(0,self.total_transactions):
            Transaction (
                transaction_id = uuid.uuid4(),
                app_id = ServiceApp.objects.order_by('?').first(),
                transaction_type = random.choice(tr_types),
                status = random.choice(tr_status),
                response_code = 200,
            ).save()
            
        