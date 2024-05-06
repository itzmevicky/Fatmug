from .models import *
from django.db.models import Q , F , Avg
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
    delivery_rate = 0.0
    vendor = purchase_order.vendor
    
    po_completed_on_before = PurchaseOrder.objects.filter(
            vendor=vendor,
            actual_delivered_date__lte=F('delivery_date'),
            status='completed'
        ).count()
        
    po_completed_total = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed'
    ).count()
    
    # print('Total ',po_completed_total )
    
    if po_completed_total > 0:
        delivery_rate = (po_completed_on_before / po_completed_total) * 100
    
    
    vendor.on_time_delivery_rate = delivery_rate 
    vendor.save()
    
def calculate_Rating_Time(purchase_order):
    vendor = purchase_order.vendor    
    rating = PurchaseOrder.objects.filter(
        vendor=vendor
    ).aggregate(
        Avg('quality_rating')
    )
    vendor.quality_rating_avg = rating * 100
    vendor.save()
    
def calculate_Fullfiment_Rate(purchase_order):
    delivery_rate = 0.0
    vendor = purchase_order.vendor
    
    po_completed = PurchaseOrder.objects.filter(
        vendor=vendor,
        status = 'completed'
    ).count()
    
    total_po = PurchaseOrder.objects.filter(vendor=vendor).count()
    
    if po_completed > 0:
        delivery_rate = (po_completed / total_po) * 100
    
    vendor.fulfillment_rate = delivery_rate
    vendor.save()

    

@receiver(post_save_signal)
def Purchase_Order_Signal(sender,instance , **kwarg):

    signal_type = kwarg.get('type')
    
    if signal_type == 'order_approved':
        calculate_Response_Time(instance)

    if signal_type == 'order_delivered':
        calculate_Delivery_Rate(instance)
    
    if signal_type == "order_cancel":
        calculate_Fullfiment_Rate(instance)
    
    if signal_type == "order_rate":
        calculate_Rating_Time(instance)
        
    
    
    




