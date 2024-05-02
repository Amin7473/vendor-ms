"""models for vendors app"""

import uuid
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import F
from vendors.utils import PoStatusEnum, generate_po_number


class TimeStampModel(models.Model):
    """Base model to store creation time details"""

    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        """meta attributes of model"""
        abstract = True


class VendorModel(TimeStampModel):
    """Model to store vendor details"""

    name = models.CharField(max_length=70, null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    vendor_code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)


class PurchaseOrderModel(TimeStampModel):
    """Model to store purchase order of each vendor"""

    po_number = models.CharField(default=generate_po_number, max_length=30 ,editable=False, unique=True)
    vendor = models.ForeignKey(
        VendorModel,
        on_delete=models.CASCADE,
        related_name='PurchaseOrderModel_vendor',
        null=True,
        blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    status = models.CharField(default='PENDING', max_length=20, choices=PoStatusEnum.choices())
    completed_date = models.DateTimeField(null=True, blank=True)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

@receiver(post_save, sender=PurchaseOrderModel)
def purchase_order_model_post_save_signal(sender, instance, **kwargs):
    """generating analytics after save"""
    print(1)
    if instance.vendor:
        print(2)
        analytics_dict = {}
        all_pos = PurchaseOrderModel.objects.filter(vendor = instance.vendor)
        completed_on_time = PurchaseOrderModel.objects.filter(
            vendor = instance.vendor,
            status = "COMPLETED",
            completed_date__lte = F('delivery_date')
        ).count()
        completed_count = PurchaseOrderModel.objects.filter(
            vendor = instance.vendor,status = "COMPLETED").count()
        if completed_count != 0:
            print(3)
            analytics_dict["on_time_delivery_rate"] = round(completed_on_time/completed_count, 2)
            quality_ratings = 0
            for obj in PurchaseOrderModel.objects.filter(
                vendor = instance.vendor,status = "COMPLETED"):
                quality_ratings += obj.quality_rating
            analytics_dict['quality_rating_avg'] = round(quality_ratings/completed_count, 2)
        if all_pos.count() != 0:
            print(4)
            avg_res_time = 0
            for obj in all_pos:
                if obj.acknowledgment_date != None and obj.issue_date != None:
                    avg_res_time += (obj.acknowledgment_date - obj.issue_date).seconds
            analytics_dict['average_response_time'] = round(avg_res_time/all_pos.count(), 2)
            analytics_dict['fulfillment_rate'] = round(completed_count/all_pos.count(), 2)
        print(5)
        VendorModel.objects.filter(id = instance.vendor.id).update(**analytics_dict)

class HistoricalPerformanceModel(TimeStampModel):
    """Model to optionally store Vendor performance history"""

    vendor = models.ForeignKey(
        VendorModel, on_delete=models.CASCADE, related_name='HistoricalPerformanceModel_vendor')
    date = models.DateTimeField(null=True, blank=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)
