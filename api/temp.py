order_type = 'HELLO'

if order_type == 'order_approved':
        if instance.acknowledgment_date:                
            self._mesg.update({
                'status':False,
                'mesg' : f'Purchase Order Id {instance.po_number} Already Approved'
            })
            return Response(self._mesg,status=status.HTTP_400_BAD_REQUEST)
        
        
        instance.acknowledgment_date = timezone.now()
        
        serializer.save()
                            
        self._mesg.update({
            'status':True,
            'mesg' :  'Order Acknowledged',
            'data' : serializer.data,
        })
        post_save_signal.send(sender=instance.__class__ , instance=instance,type=order_type)
        return Response(self._mesg,status=status.HTTP_200_OK)     
elif order_type == 'order_delivered' :
    
        if not instance.acknowledgment_date:
            self._mesg.update({
                'status' :False,
                'mesg' : 'Approve , Purchase Order First'
            })
            return Response(self._mesg,status=status.HTTP_400_BAD_REQUEST)
        
        if instance.status == 'completed':
            self._mesg.update({
                'status' :False,
                'mesg' : 'Invalid , Order Already Delivered'
            })
            return Response(self._mesg,status=status.HTTP_400_BAD_REQUEST)
        
        

        instance.status = 'completed'
        instance.actual_delivered_date = timezone.now()
        
        serializer.save()
        
        self._mesg.update({
            'status':True,
            'mesg' :  'Order Completed',
        })
        post_save_signal.send(sender=instance.__class__ , instance=instance,type=order_type)
        return Response(self._mesg,status=status.HTTP_200_OK)    
else:
    self._mesg.update({
        'mesg' : "Invalid , must pass 'type' in params",
        'status' :False,
    })
    return Response(self._mesg,status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        