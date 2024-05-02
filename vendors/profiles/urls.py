"""urls for vendors app"""

from django.urls import path
from vendors.profiles import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('api-token-auth/',
         auth_view.obtain_auth_token,
         name='api-token-auth'),

    path('create-vendor-api/',
         views.CreateVendorAPIView.as_view(),
         name='CreateVendorAPIView'),

    path('update-vendor-api/<pk>/',
         views.UpdateVendorAPIView.as_view(),
         name='UpdateVendorAPIView'),

    path('vendor-list-api/',
         views.VendorListAPIView.as_view(),
         name='VendorListAPIView'),

    path('get-vendor-info-api/<pk>/',
         views.GetVendorInfoAPIView.as_view(),
         name='GetVendorInfoAPIView'),

    path('delete-vendor-api/<pk>/',
         views.DeleteVendorAPIView.as_view(),
         name='DeleteVendorAPIView'),

    path('vendor-performance-api/<pk>/',
         views.VendorPerformanceAPIView.as_view(),
         name='VendorPerformanceAPIView'),
]
