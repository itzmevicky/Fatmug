from django.urls import path
from .views import Get_Create_Vendors

urlpatterns = [
    path('vendors/',Get_Create_Vendors.as_view(),name='Create_Get_Vendors')
]