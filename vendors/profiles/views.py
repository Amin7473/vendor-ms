"""Views for vendors app"""

from rest_framework import views, generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from vendors.models import VendorModel, PurchaseOrderModel
from vendors.profiles.serializers import (CreateVendorSerializer,
                                 DeleteVendorSerializer,
                                 UpdateVendorSerializer,
                                 VendorListSerializer, VendorPerformanceSerializer,)


class CreateVendorAPIView(views.APIView):
    """API to create new vendor"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """POST method"""
        try:
            data = request.data
            serializer = CreateVendorSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'Vendor added'}, status=status.HTTP_200_OK)
            else:
                return Response({'message' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateVendorAPIView(views.APIView):
    """API to update vendor"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        """PUT method"""
        try:
            data = request.data
            data['id'] = pk
            serializer = UpdateVendorSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'Vendor updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'message' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class VendorListAPIView(generics.ListAPIView):
    """Get list of vendors"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = VendorModel.objects.all()
    serializer_class = VendorListSerializer

    def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(
                self.paginate_queryset(self.get_queryset()), many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetVendorInfoAPIView(views.APIView):
    """API to get vendor info"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = VendorModel.objects.all()
    serializer_class = VendorListSerializer

    def get(self, request, pk):
        """GET method"""
        try:
            serializer = self.serializer_class(self.queryset.get(id=pk), many=False)
            return Response({'message' : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteVendorAPIView(views.APIView):
    """API to delete vendor"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        """DELETE method"""
        try:
            serializer = DeleteVendorSerializer(data = {'id' : pk})
            if serializer.is_valid():
                serializer.save()
                return Response({'message' : 'Vendor deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'message' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)

class VendorPerformanceAPIView(views.APIView):
    """API to get vendor performance"""
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = VendorModel.objects.all()
    serializer_class = VendorPerformanceSerializer

    def get(self, request, pk):
        """GET method"""
        try:
            serializer = self.serializer_class(self.queryset.get(id=pk), many=False)
            return Response({'message' : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message' : str(e)}, status=status.HTTP_400_BAD_REQUEST)
