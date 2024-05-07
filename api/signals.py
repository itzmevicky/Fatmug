from .models import *
from django.db.models import  F , Avg , Count , Case , When , IntegerField
from django.dispatch import Signal , receiver

from .utilis import Calculate

post_save_signal = Signal()






# def calculate_Response_Time(purchase_order):
#         vendor = purchase_order.vendor
#         new_duration = (purchase_order.acknowledgment_date - purchase_order.issue_date).total_seconds() / 3600.0
#         avg_response_time, created = AverageResponseTime.objects.get_or_create(
#             vendor=vendor
#         )
#         if avg_response_time.count == 0:
#             vendor.average_response_time = new_duration
#             avg_response_time.count = 1  
#         else:
#             total_duration = vendor.average_response_time * avg_response_time.count
#             total_duration += new_duration
#             avg_response_time.count += 1  
#             vendor.average_response_time = total_duration / avg_response_time.count
            
#         avg_response_time.save()
#         vendor.save()
        
# def calculate_Delivery_Rate(purchase_order):    
#     delivery_rate = 0.0
#     vendor = purchase_order.vendor
    
#     result = PurchaseOrder.objects.filter(
#             vendor=vendor,
#             status='completed'
#         ).aggregate(
#             po_completed_total=Count('po_number'), 
#             po_completed_on_before=Count(Case(
#                 When(actual_delivered_date__lte=F('delivery_date'), then=1)  
#             ))
#         )
        
#     po_completed_on_before, po_completed_total = result.values()
    
    
#     if po_completed_total > 0:
#         delivery_rate = (po_completed_on_before / po_completed_total) * 100
    
    
#     vendor.on_time_delivery_rate = delivery_rate 
#     vendor.save()
    
# def calculate_Rating_Time(purchase_order):
#     vendor = purchase_order.vendor    
    
#     rating = PurchaseOrder.objects.filter(
#         vendor=vendor
#     ).aggregate(
#         Avg('quality_rating')
#     )    
#     vendor.quality_rating_avg = rating.get('quality_rating__avg')
#     vendor.save()
    
# def calculate_Fullfiment_Rate(purchase_order):
#     delivery_rate = 0.0
#     vendor = purchase_order.vendor
        
#     vendor_data = PurchaseOrder.objects.filter(
#         vendor=vendor
#     ).aggregate(
#         total_po=Count('po_number'),  
#         po_completed=Count(
#             Case(
#                 When(status='completed', then=1),
#                 output_field=IntegerField()
#             )
#         )
#     )
#     po_completed , total_po = vendor_data.values()
    
    
    
#     if po_completed > 0:
#         delivery_rate = (po_completed / total_po) * 100
    
#     vendor.fulfillment_rate = delivery_rate
#     vendor.save()


class Calculate_ResponseTime(Calculate):
    def __init__(self, instance) -> None:
        super().__init__(instance)
        self.calculate()
        
    def calculate(self):
        self._vendor        
        new_duration = (self._vendor.acknowledgment_date - self._vendor.issue_date).total_seconds() / 3600.0
        avg_response_time, created = AverageResponseTime.objects.get_or_create(
            vendor=self._vendor.vendor
        )
        if avg_response_time.count == 0:
            self._vendor.vendor.average_response_time = new_duration
            avg_response_time.count = 1  
        else:
            total_duration = self._vendor.vendor.average_response_time * avg_response_time.count
            total_duration += new_duration
            avg_response_time.count += 1  
            self._vendor.vendor.average_response_time = total_duration / avg_response_time.count
            
        avg_response_time.save()
        self._vendor.save()
        
class Calculate_Delivery_Rate(Calculate):
    def __init__(self, instance) -> None:
        super().__init__(instance)
        self.calculate()
    
    def calculate(self):
        delivery_rate = 0.0
        
        result = PurchaseOrder.objects.filter(
            vendor=self._vendor,
            status='completed'
        ).aggregate(
            po_completed_total=Count('po_number'), 
            po_completed_on_before=Count(Case(
                When(actual_delivered_date__lte=F('delivery_date'), then=1)  
            ))
        )        
        po_completed_on_before, po_completed_total = result.values()        
        
        if po_completed_total > 0:
            delivery_rate = (po_completed_on_before / po_completed_total) * 100
        
        
        self._vendor.on_time_delivery_rate = delivery_rate 
        self._vendor.save()
        
class Calculate_Rating_Time(Calculate):
    
    def __init__(self, instance) -> None:
        super().__init__(instance)
        self.calculate()      
        
    def calculate(self):     
        rating = PurchaseOrder.objects.filter(
            vendor=self._vendor
        ).aggregate(
            Avg('quality_rating')
        )    
        self._vendor.quality_rating_avg = rating.get('quality_rating__avg')
        self._vendor.save()

class Calculate_Fullfilment_Rate(Calculate):
    
    def __init__(self, instance) -> None:
        super().__init__(instance)
        self.calculate()
    
    def calculate(self):
        delivery_rate = 0.0
            
        vendor_data = PurchaseOrder.objects.filter(
            vendor=self._vendor
        ).aggregate(
            total_po=Count('po_number'),  
            po_completed=Count(
                Case(
                    When(status='completed', then=1),
                    output_field=IntegerField()
                )
            )
        )
        po_completed , total_po = vendor_data.values()
        
        
        
        if po_completed > 0:
            delivery_rate = (po_completed / total_po) * 100
        
        self._vendor.fulfillment_rate = delivery_rate
        self._vendor.save()
        

@receiver(post_save_signal)
def Purchase_Order_Signal(sender,instance , **kwarg):

    signal_type = kwarg.get('type')
    
    if signal_type == 'order_approved':        
        Calculate_ResponseTime(instance)

    if signal_type == 'order_delivered':        
        Calculate_Delivery_Rate(instance)
        Calculate_Fullfilment_Rate(instance)
    
    if signal_type == "order_cancel":
        Calculate_Fullfilment_Rate(instance)
    
    if signal_type == "order_rate":
        Calculate_Rating_Time(instance)
        
    
    
    




