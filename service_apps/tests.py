from django.test import TestCase
from service_apps.models import ServiceApp
from service_transactions.models import Transaction
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self) -> None:
        User.objects.create(username="test_user",email="test_user@gmail.com")
        test_user = User.objects.first()
        ServiceApp.objects.create(creator = test_user.username,app_id="1234", active = True)
        test_service = ServiceApp.objects.first()
        Transaction.objects.create(transaction_id = "TR11", app_id=test_service, transaction_type="AIRTIME")
        Transaction.objects.create(transaction_id = "TR12", app_id=test_service, transaction_type="PAYBILL")
        Transaction.objects.create(transaction_id = "TR13", app_id=test_service, transaction_type="BUY_GOODS")
        Transaction.objects.create(transaction_id = "TR14", app_id=test_service, transaction_type="SEND_MONEY")

    def test_models(self):
        all_transactions = Transaction.objects.all().count()
        send_money_tr = Transaction.objects.filter(transaction_id = "TR14").first()

        self.assertEqual(all_transactions, 4)
        self.assertEqual(send_money_tr.transaction_type, "SEND_MONEY")
        print("\n---- INIT CREATION TEST ----")

# To test ; python3 manage.py test apps.entities.tests

