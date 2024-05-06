from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/',Get_Create_Vendors.as_view(),name='Create_Get_Vendors'),
    path("login/", Login.as_view(), name="login"),
    
    path('vendors/<int:pk>',Update_Delete_Vendors.as_view(),name='Update_Delete_Vendors'),
    path('vendors/<int:pk>/performance',Get_Vendor_Performance.as_view(),name='Update_Delete_Vendors'),
    

    path("purchase_orders/", Get_Create_Order.as_view(), name="Create_Get_PO"),
    path("purchase_orders/<int:pk>/", Update_Delete_Order.as_view(), name="Update_Delete_PO"),   
    path("purchase_orders/<int:pk>/acknowledge/",AcknowledgeOrder.as_view(),name="acknolwedge_orders") ,
    
    path("randomproducts/", GenerateRandomProducts.as_view(), name="Random_Product"),
]