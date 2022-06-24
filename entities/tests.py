from django.test import TestCase
from .models import Transaction, ServiceApps
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self) -> None:
        mm = User.objects.first()
        ServiceApps.objects.create(creator = mm,app_id="1234", active = 'YES')
        Transaction.objects.create(transaction_id = "TR1", app_id="1234", transaction_type="AIRTIME")
        Transaction.objects.create(transaction_id = "TR12", app_id="1234", transaction_type="PAYBILL")
        Transaction.objects.create(transaction_id = "TR13", app_id="1234", transaction_type="BUY_GOODS")
        Transaction.objects.create(transaction_id = "TR14", app_id="1234", transaction_type="SEND_MONEY")

    def test_models(self):
        all_transactions = Transaction.objects.all().count()
        send_money_tr = Transaction.objects.filter(transaction_id = "TR14").first()


        self.assertEqual(all_transactions, 4)
        self.assertEqual(send_money_tr.transaction_type, "SEND_MONEY")

# To test ; python3 manage.py test apps.entities.tests

