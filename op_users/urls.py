from django.urls import path
from .views import Generator

urlpatterns = [ 
    path("seed/", Generator.as_view(), name="seed-apps-and-transactions")
]