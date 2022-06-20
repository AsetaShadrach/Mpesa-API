from random import seed
from django.test import TestCase
from .views import MpesaExpress
from .models import Transaction, Application

class TestModels(TestCase):
    def setUp(self) -> None:
        Transaction.objects.create()
        Application.objects.create()
        Transaction.objects.create()
        Transaction.objects.create()
        Application.objects.create()
        Transaction.objects.create()


