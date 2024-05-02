from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from django.utils import timezone
from django.db.models import Count, Avg, F

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=Vendor)
def create_vendor_performance_history(sender, instance, created, **kwargs):
    if created:
        HistoricalPerformance.objects.create(
            vendor=instance,
            date=timezone.now(),
            on_time_delivery_rate=0,
            quality_rating_avg=0,
            average_response_time=0,
            fulfillment_rate=0
        )

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, created, **kwargs):
    if instance.vendor:
        update_vendor_performance_metrics(instance.vendor)
        update_vendor_performance_history(instance.vendor, timezone.now())

def update_vendor_performance_metrics(vendor):
    total_completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    if total_completed_pos > 0:
        on_time_delivery_rate = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=F('acknowledgment_date')).count() / total_completed_pos * 100
        quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, status='completed').aggregate(Avg('quality_rating'))['quality_rating__avg']
        average_response_time = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response_time']
        fulfillment_rate = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count() / PurchaseOrder.objects.filter(vendor=vendor).count() * 100
        
        if average_response_time is not None:  # Check if average_response_time is not None
            # Convert timedelta to number of days
            average_response_time = average_response_time.total_seconds() / (60 * 60 * 24)
        else:
            average_response_time = 0

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg or 0
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()


def update_vendor_performance_history(vendor, date):
    performance_record = HistoricalPerformance.objects.create(
        vendor=vendor,
        date=date,
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate
    )


