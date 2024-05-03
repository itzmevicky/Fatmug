from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.utils import timezone
from .models import *
import datetime


class UserSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = User
        fields = ['id','name','email', 'password' ]
 

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.fields['password'].required = True
        else:
            self.fields['password'].required = False
    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['pk'] = instance.id
        rep.pop('id')
        return rep
        
class ModifyUserSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model =  Vendor
        fields = ['user','contact_details','address']

        
    def __init__(self, *args, **kwargs):
        super(ModifyUserSerializer, self).__init__(*args, **kwargs)
        self.fields['user'] = UserSerializer(context=self.context)

    def create(self, validated_data):
        user_data = validated_data.pop('user')        
        user_data['username']  = user_data['email'] 
        
        if 'password' not in user_data.keys():
            raise serializers.ValidationError({'password' : 'password missing in the request'})
                
        user_data['password'] = make_password(user_data['password'])          
        user = User.objects.create(**user_data)       
        Vendor.objects.create(user=user, **validated_data)
        return user
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})        
        user_serializer = UserSerializer(instance.user,data=user_data, partial=True)                
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()        
        return super(ModifyUserSerializer, self).update(instance, validated_data)
            
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['vendor_code'] = instance.vendor_code
        rep.get('user').pop('password')
        return rep

class OrderSerializer(serializers.ModelSerializer):
    delivery_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ", required=False)

    class Meta:
        model = PurchaseOrder
        fields = ['po_number','items','quantity','vendor' , 'delivery_date','acknowledgment_date' ]
    
    def create(self, validated_data):
        validated_data['delivery_date'] = timezone.now() + datetime.timedelta(days=2)
        return PurchaseOrder.objects.create(**validated_data)

    def update(self, instance, validated_data):      
        
        if instance.acknowledgment_date:
            raise  serializers.ValidationError(f'Order Id {instance.po_number} Already Approved')     
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value) 
                    
        instance.acknowledgment_date = timezone.now()
        instance.save()     
        
        return instance
    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        
        rep.update({
            'vendor' : ModifyUserSerializer(instance.vendor).data.get('user').get('name') if instance.vendor and instance.vendor.user else 'No Vendor',
            'po_number' :instance.po_number,
            'issue_date' : instance.issue_date.strftime("%d-%m-%Y %H:%M"),
            'delivery_date' : instance.delivery_date.strftime('%d-%m-%Y'),
            'status' : instance.status,
            'acknowledgment_date' : instance.acknowledgment_date.strftime("%d-%m-%Y %H:%M") if instance.acknowledgment_date else 'Waiting for confirmation',
        })
        return rep