from django.urls import path, include
from rest_framework.routers import DefaultRouter
from suppliers.views import SupplierViewSet
from suppliers.apps import SuppliersConfig

app_name = SuppliersConfig.name

suppliers_router = DefaultRouter()
suppliers_router.register(r'suppliers', SupplierViewSet, basename='suppliers')

urlpatterns = [
    path('', include(suppliers_router.urls)),
]
