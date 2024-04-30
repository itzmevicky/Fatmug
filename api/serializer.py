from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *


class UserSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = User
        fields = ['name','email', 'password' ]
 

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.fields['password'].required = True
        else:
            self.fields['password'].required = False
        
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
