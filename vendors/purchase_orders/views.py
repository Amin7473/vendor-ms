"""Views for vendors app"""

from rest_framework import views, generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from vendors.models import VendorModel, PurchaseOrderModel
from vendors.purchase_orders.serializers import (AcknowledgePurchaseOrderSerializer, CreatePurchaseOrderSerializer,
                                                 UpdatePurchaseOrderSerializer,
                                                 PurchaseOrderListSerializer,
                                                 DeletePurchaseOrderSerializer)


class CreatePurchaseOrderAPIView(views.APIView):
    """API to create new purchase order"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """POST method"""
        try:
            data = request.data
            serializer = CreatePurchaseOrderSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'Purchase order created'}, status=status.HTTP_200_OK)
            else:
                return Response({'message' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePurchaseOrderAPIView(views.APIView):
    """API to update purchase order"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        """PUT method"""
        try:
            data = request.data
            data['id'] = pk
            serializer = UpdatePurchaseOrderSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'Purchase order updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'message' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderListAPIView(generics.ListAPIView):
    """Get list of purchase orders"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderListSerializer

    def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(
                self.paginate_queryset(self.get_queryset()), many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetPurchaseOrderInfoAPIView(views.APIView):
    """API to get purchase order info"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderListSerializer

    def get(self, request, pk):
        """GET method"""
        try:
            serializer = self.serializer_class(self.queryset.get(id=pk), many=False)
            return Response({'message' : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DeletePurchaseOrderAPIView(views.APIView):
    """API to delete purchase order"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        """DELETE method"""
        try:
            serializer = DeletePurchaseOrderSerializer(data = {'id' : pk})
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'Purchase order deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'message' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AcknowledgePurchaseOrderAPIView(views.APIView):
    """API to acknowledge purchase order"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        """DELETE method"""
        try:
            serializer = AcknowledgePurchaseOrderSerializer(data = {'id' : pk})
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'Purchase order acknowledged'}, status=status.HTTP_200_OK)
            else:
                return Response({'message' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
