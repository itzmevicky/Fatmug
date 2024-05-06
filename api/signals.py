from .models import *
from django.db.models import Q
from django.dispatch import Signal , receiver



post_save_signal = Signal()


def calculate_Response_Time(purchase_order):
        vendor = purchase_order.vendor
        new_duration = (purchase_order.acknowledgment_date - purchase_order.issue_date).total_seconds() / 3600.0
        avg_response_time, created = AverageResponseTime.objects.get_or_create(
            vendor=vendor
        )

        if avg_response_time.count == 0:
            vendor.average_response_time = new_duration
            avg_response_time.count = 1  
        else:
            total_duration = vendor.average_response_time * avg_response_time.count
            total_duration += new_duration
            avg_response_time.count += 1  
            vendor.average_response_time = total_duration / avg_response_time.count
            
        avg_response_time.save()
        vendor.save()
        
def calculate_Delivery_Rate(purchase_order):
    vendor = purchase_order.vendor
    
    PurchaseOrder.objects.filter( Q( vendor=vendor) & ( Q(issue_date__lte = vendor.actual_delivered_date) | Q(issue_date=vendor.actual_delivered_date)) )
    
    
    
    




@receiver(post_save_signal)
def Purchase_Order_Signal(sender,instance , **kwarg):

    signal_type = kwarg.get('type')
    
    if signal_type == 'order_approved':
        calculate_Response_Time(instance)

    elif signal_type == 'order_delivered':
        calculate_Delivery_Rate(instance)
    




