from django.urls import path
from . import views

urlpatterns = [ 
    path("seed/data/", views.SeedDataGenerator.as_view(), name="seed_apps_and_transactions"),
    path("user/create/", views.CreateUser.as_view(), name= "create_user"),
    path("user/list", views.GetAllUsers.as_view(), name= "list_users")
]