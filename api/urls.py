from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/',Get_Create_Vendors.as_view(),name='Create_Get_Vendors'),

]