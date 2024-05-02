"""serializers for vendors app"""

from rest_framework import serializers
from vendors.models import VendorModel, PurchaseOrderModel

class CreateVendorSerializer(serializers.Serializer):
    """Serializer for creating vendor"""
    name = serializers.CharField(required = True)
    contact_details = serializers.CharField(required = True)
    address = serializers.CharField(required = True)

    def create(self, validated_data):
        """create method"""
        VendorModel.objects.create(**validated_data)
        return validated_data

class UpdateVendorSerializer(serializers.Serializer):
    """Serializer for updating vendor"""
    id = serializers.IntegerField(required = True)
    name = serializers.CharField(required = True)
    contact_details = serializers.CharField(required = True)
    address = serializers.CharField(required = True)


    def validate(self, attrs):
        """validate method"""
        if not VendorModel.objects.filter(id=attrs['id']).exists():
            raise serializers.ValidationError('Vendor with this id does not exist')
        return attrs

    def create(self, validated_data):
        """create method"""
        pk = validated_data['id']
        validated_data.pop('id')
        VendorModel.objects.filter(id=pk).update(**validated_data)
        return validated_data

class VendorListSerializer(serializers.ModelSerializer):
    """Serializer for listing vendors"""

    class Meta:
        """meta attributes"""
        model = VendorModel
        fields = '__all__'


class DeleteVendorSerializer(serializers.Serializer):
    """Serializer for deleteing vendor"""
    id = serializers.IntegerField(required=True)

    def validate(self, attrs):
        """validate method"""
        if not VendorModel.objects.filter(id=attrs['id']).exists():
            raise serializers.ValidationError('Vendor with this id does not exist')
        return attrs

    def create(self, validated_data):
        """create method"""
        pk = validated_data['id']
        validated_data.pop('id')
        VendorModel.objects.filter(id=pk).delete()
        return validated_data

class VendorPerformanceSerializer(serializers.ModelSerializer):
    """Serializer for getting vendor performance"""

    class Meta:
        """meta attributes"""
        model = VendorModel
        fields = [
            'id',
            'on_time_delivery_rate',
            'quality_rating_avg',
            'average_response_time',
            'fulfillment_rate'
        ]
