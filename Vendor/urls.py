"""
URL configuration for TASK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from App.views import VendorViewSet, PurchaseOrderViewSet,performacematrixViewSet
from App.auth import CustomAuthToken

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'historicat_performance',performacematrixViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('gettoken/',CustomAuthToken.as_view())
    # path('api/vendors/', views.create_vendor),
    # path('api/List/', views.list_vendors),
    # path('api/vendors/<int:vendor_id>/', views.vendor_detail),
    # path('api/purchase_orders/', views.create_purchase_order),
    # path('api/Purchase_List/', views.list_purchase_orders),
    # path('api/purchase_orders/<int:po_id>/', views.purchase_order_detail),
    # path('api/vendors/<int:vendor_id>/performance/', views.get_vendor_performance),
    # path('api/vendors/<int:vendor_id>/historical-performance/', views.get_vendor_historical_performance),
]

