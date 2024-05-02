from rest_framework import viewsets
from .models import Vendor, PurchaseOrder,HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer,HistoricalPerformanceSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
class performacematrixViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    
