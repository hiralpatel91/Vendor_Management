from django.contrib import admin
from .models import HistoricalPerformance,PurchaseOrder,Vendor
# Register your models here.


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ("fulfillment_rate", "average_response_time", "quality_rating_avg", "on_time_delivery_rate", "date", "vendor")


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ("acknowledgment_date", "issue_date", "quality_rating", "status", "quantity", "items", "delivery_date", "order_date", "vendor", "po_number")


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("fulfillment_rate", "average_response_time", "quality_rating_avg", "on_time_delivery_rate", "vendor_code", "address", "contact_details", "name")


