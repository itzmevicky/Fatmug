from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    class Meta :
        model = User
        fields = ['email','name', 'contact_details','password']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('password')
        rep['vendor_code'] = instance.vendor_code
        return rep
        
