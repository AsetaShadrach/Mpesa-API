"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from decouple import config

from settings.development import DEBUG

schema_view = get_schema_view(
   openapi.Info(
      title="MPESA API",
      default_version='v1',
      description="Mpesa django api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="asetashadrach@gmail.com"),
      license=openapi.License(name="License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # API docs
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/services/', include('service_apps.urls')),
    path('api/transactions/', include('service_transactions.urls')),
    path('api/operations/', include('op_users.urls')),
]


if config('DEBUG'):
    # silk profiler
    urlpatterns.append( path('silk/', include('silk.urls')),)
