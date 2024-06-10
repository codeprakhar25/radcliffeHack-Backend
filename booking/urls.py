# urls.py

from django.urls import path
from .views import AllInventory, AllTests, InventoryListCreateView, InventoryRetrieveUpdateDestroyView, TestListCreateView, TestRetrieveUpdateDestroyView, InventoryTestListView

urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<uuid:uuid>/', InventoryRetrieveUpdateDestroyView.as_view(), name='inventory-detail'),
    path('tests/', TestListCreateView.as_view(), name='test-list-create'),
    path('all-tests/', AllTests.as_view(), name='all-test'),
    path('all-inventory/', AllInventory.as_view(), name='all-inventory'),
    path('tests/<uuid:uuid>/', TestRetrieveUpdateDestroyView.as_view(), name='test-detail'),
    path('inventory/<uuid:inventory_uuid>/tests/', InventoryTestListView.as_view(), name='inventory-test-list'),
]
