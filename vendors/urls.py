"""urls for vendors app"""

from django.urls import path, include

urlpatterns = [
    path("api/profiles/v1/", include("vendors.profiles.urls")),
    path("api/purchase_orders/v1/", include("vendors.purchase_orders.urls")),
]
