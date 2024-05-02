from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/',Get_Create_Vendors.as_view(),name='Create_Get_Vendors'),
    path("login/", Login.as_view(), name="login"),
    path('vendors/<int:pk>',Update_Delete_Vendors.as_view(),name='Update_Delete_Vendors'),
]