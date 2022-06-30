from django.urls import path
from .views import SeedDataGenerator

urlpatterns = [ 
    path("seed/", SeedDataGenerator.as_view(), name="seed-apps-and-transactions")
]