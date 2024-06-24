# views.py

from rest_framework import generics, permissions
from .models import Inventory, Test
from .serializers import InventorySerializer, TestSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class InventoryListCreateView(generics.ListCreateAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Inventory.objects.filter(user=self.request.user)

class InventoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def get_queryset(self):
        return Inventory.objects.all()
    
    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

class TestListCreateView(generics.ListCreateAPIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Test.objects.filter(user=self.request.user)

class TestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def get_queryset(self):
        return Test.objects.all()
    
    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

class InventoryTestListView(generics.ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        inventory_uuid = self.kwargs['inventory_uuid']
        return Test.objects.filter(inventory__uuid=inventory_uuid)

class AllInventory(generics.ListAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Inventory.objects.all().order_by('-created_at')
    
class AllTests(generics.ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Test.objects.all().order_by('-created_at')
    
class InventoryRetrieveUpdateDestroyViewbyId(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Inventory.objects.all()
    
class TestRetrieveUpdateDestroyViewbyId(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Test.objects.all()