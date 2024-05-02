"""serializers for vendors app"""

import datetime
import pytz
from rest_framework import serializers
from vendors.models import VendorModel, PurchaseOrderModel

class CreatePurchaseOrderSerializer(serializers.Serializer):
    """Serializer for creating purchase order"""
    delivery_date = serializers.DateTimeField(required = True)
    items = serializers.JSONField(required = True)
    quantity = serializers.IntegerField(required = True)

    def create(self, validated_data):
        """create method"""
        validated_data['order_date'] = datetime.datetime.now(pytz.utc)
        PurchaseOrderModel.objects.create(**validated_data)
        return validated_data

class UpdatePurchaseOrderSerializer(serializers.Serializer):
    """Serializer for updating purchase order"""
    id = serializers.IntegerField(required = True)
    vendor_id = serializers.IntegerField(required = False)
    status = serializers.CharField(required = False)
    quality_rating = serializers.IntegerField(required = False)
    items = serializers.JSONField(required= True)
    quantity = serializers.IntegerField(required= True)

    def validate(self, attrs):
        """validate method"""
        if not PurchaseOrderModel.objects.filter(id=attrs['id']).exists():
            raise serializers.ValidationError('Purchase order with this id does not exist')
        return attrs

    def create(self, validated_data):
        """create method"""
        pk = validated_data['id']
        po_instance = PurchaseOrderModel.objects.get(id = pk)
        validated_data.pop('id')
        if validated_data.get("status") == "COMPLETED":
            validated_data["completed_date"] = datetime.datetime.now(pytz.utc)
        if not po_instance.vendor and validated_data.get("vendor_id") not in [None, ""]:
            validated_data["issue_date"] = datetime.datetime.now(pytz.utc)
        print(pk, validated_data)
        PurchaseOrderModel.objects.filter(id=pk).update(**validated_data)
        po_instance = PurchaseOrderModel.objects.get(id = pk)
        po_instance.save()
        return validated_data

class PurchaseOrderListSerializer(serializers.ModelSerializer):
    """Serializer for listing purchase orders"""

    class Meta:
        """meta attributes"""
        model = PurchaseOrderModel
        fields = '__all__'


class DeletePurchaseOrderSerializer(serializers.Serializer):
    """Serializer for deleteing purchase order"""
    id = serializers.IntegerField(required=True)

    def validate(self, attrs):
        """validate method"""
        if not PurchaseOrderModel.objects.filter(id=attrs['id']).exists():
            raise serializers.ValidationError('Purchase order with this id does not exist')
        return attrs

    def create(self, validated_data):
        """create method"""
        pk = validated_data['id']
        validated_data.pop('id')
        PurchaseOrderModel.objects.filter(id=pk).delete()
        return validated_data

class AcknowledgePurchaseOrderSerializer(serializers.Serializer):
    """Serializer for acknowledging purchase order"""
    id = serializers.IntegerField(required=True)

    def validate(self, attrs):
        """validate method"""
        if not PurchaseOrderModel.objects.filter(id=attrs['id']).exists():
            raise serializers.ValidationError('Purchase order with this id does not exist')
        return attrs

    def create(self, validated_data):
        """create method"""
        pk = validated_data['id']
        validated_data.pop('id')
        PurchaseOrderModel.objects.filter(id=pk).update(
            acknowledgment_date = datetime.datetime.now(pytz.utc)
        )
        po_instance = PurchaseOrderModel.objects.get(id = pk)
        po_instance.save()
        return validated_data