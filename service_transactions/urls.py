from django.urls import path
from . import views

urlpatterns = [
    path('transaction/mpesa-express/', views.MpesaExpress.as_view(), name="mpesa_express"),
    path('transaction/sendmoney/', views.SendMoney.as_view(), name="send_money"),
    path('transaction/reversal/', views.ReverseSendMoney.as_view(), name="reverse_send_money"),
    path('transaction/mpesa-callbackurl/', views.MpesaCallbackUrl.as_view(), name = "mpesa_callback_url"),
    path('list', views.TransactionsList.as_view(),name="get_transactions_list"),
    path('details/<transaction_id>', views.TransactionDetail.as_view(), name="get_transaction_details"),
    path('details/filter/', views.FilterTansactions.as_view(), name="filter_transactions"),
    ]