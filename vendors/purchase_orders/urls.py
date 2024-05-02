"""urls for vendors app"""

from django.urls import path
from vendors.purchase_orders import views

urlpatterns = [
    path('create-purchase-order-api/',
         views.CreatePurchaseOrderAPIView.as_view(),
         name='CreatePurchaseOrderAPIView'),

    path('update-purchase-order-api/<pk>/',
         views.UpdatePurchaseOrderAPIView.as_view(),
         name='UpdatePurchaseOrderAPIView'),

    path('purchase-order-list-api/',
         views.PurchaseOrderListAPIView.as_view(),
         name='PurchaseOrderListAPIView'),

    path('get-purchase-order-info-api/<pk>/',
         views.GetPurchaseOrderInfoAPIView.as_view(),
         name='GetPurchaseOrderInfoAPIView'),

    path('delete-purchase-order-api/<pk>/',
         views.DeletePurchaseOrderAPIView.as_view(),
         name='DeletePurchaseOrderAPIView'),

    path('acknowledge-purchase-order-api/<pk>/',
         views.AcknowledgePurchaseOrderAPIView.as_view(),
         name='AcknowledgePurchaseOrderAPIView'),

]
