from django.urls import path
from . import views

urlpatterns = [
    path('list', views.ServiceAppList.as_view(), name="get_service_apps_list"),
    path('service/details/<str:app_name>', views.ServiceAppDetails.as_view(), name="get_service_detials"),
    path('service/update/', views.UpdateServiceDetails.as_view(), name='update_service_details'),
    path('service/create/', views.CreateService.as_view(), name='create_service'),
    ]