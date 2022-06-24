from django.urls import path
from . import views

urlpatterns = [
    path('mpesa-express/', views.MpesaExpress.as_view(), name="mpesa-express"),
    path('sendmoney/', views.SendMoney.as_view(), name="send-money"),
    path('reversal/', views.ReverseSendMoney.as_view(), name="reverse-send-money"),
    path('mpesa-callbackurl/', views.MpesaCallbackUrl.as_view(), name = "mpesa-callback-url")
    ]