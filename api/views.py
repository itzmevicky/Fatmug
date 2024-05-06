from abc import ABC

from .models import *
from .serializer import *
from .permissions import *

from .utilis import  getRefreshToken
from rest_framework.views import APIView  
from rest_framework import status,generics 
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .signals import *

from django.db.models import Avg, ExpressionWrapper, F, fields


import random 



class UserResponse(ABC) :
    def __init__(self) -> None:
        self._mesg = {}

class GenerateRandomProducts(APIView):
    
    def get(self, request , *args, **kwargs):
        
        products = [
            {"id": random.randint(1, 1000), "name": "iPhone", "category": "phones", "price": random.randint(35000, 100000), "description": "A smartphone from Apple."},
            {"id": random.randint(1, 1000), "name": "Samsung Galaxy", "category": "phones", "price": random.randint(25000, 75000), "description": "Latest model with high resolution camera."},
            {"id": random.randint(1, 1000), "name": "LG OLED55", "category": "tv", "price": random.randint(80000, 150000), "description": "55 inch OLED TV with smart features."},
            {"id": random.randint(1, 1000), "name": "Sony Bravia", "category": "tv", "price": random.randint(60000, 120000), "description": "Ultra HD TV with excellent sound quality."},
            {"id": random.randint(1, 1000), "name": "Brake Pads", "category": "vehicle parts", "price": random.randint(2000, 5000), "description": "Durable brake pads for any car."},
            {"id": random.randint(1, 1000), "name": "Steering Wheel Cover", "category": "vehicle parts", "price": random.randint(1500, 3000), "description": "Leather steering wheel cover."},
            {"id": random.randint(1, 1000), "name": "Banana", "category": "fruits", "price": random.randint(40, 80), "description": "A fresh yellow banana."},
            {"id": random.randint(1, 1000), "name": "Apple", "category": "fruits", "price": random.randint(120, 200), "description": "Crisp and juicy apples."},
            {"id": random.randint(1, 1000), "name": "Carrots", "category": "vegetables", "price": random.randint(50, 100), "description": "Fresh organic carrots."},
            {"id": random.randint(1, 1000), "name": "Broccoli", "category": "vegetables", "price": random.randint(70, 150), "description": "Rich in vitamins and perfect for steaming."},
            {"id": random.randint(1, 1000), "name": "Whole Wheat Bread", "category": "groceries", "price": random.randint(50, 100), "description": "Healthy whole wheat bread."},
            {"id": random.randint(1, 1000), "name": "Organic Milk", "category": "groceries", "price": random.randint(50, 100), "description": "Organic milk sourced from local farms."},
            {"id": random.randint(1, 1000), "name": "Smart Thermostat", "category": "electronics", "price": random.randint(10000, 25000), "description": "Energy-efficient thermostat with WiFi capabilities."},
            {"id": random.randint(1, 1000), "name": "Electric Scooter", "category": "transport", "price": random.randint(15000, 45000), "description": "Portable electric scooter ideal for quick urban travel."},
            {"id": random.randint(1, 1000), "name": "VR Headset", "category": "electronics", "price": random.randint(20000, 60000), "description": "Immersive VR headset for realistic gaming and simulations."},
            {"id": random.randint(1, 1000), "name": "Action Camera", "category": "electronics", "price": random.randint(8000, 20000), "description": "Compact, rugged action camera for adventure sports."},
            {"id": random.randint(1, 1000), "name": "Bluetooth Headphones", "category": "electronics", "price": random.randint(5000, 15000), "description": "High-quality sound with noise cancellation features."},
            {"id": random.randint(1, 1000), "name": "Espresso Machine", "category": "kitchenware", "price": random.randint(15000, 50000), "description": "Barista-grade espresso machine with multiple features."},
            {"id": random.randint(1, 1000), "name": "Smart Watch", "category": "electronics", "price": random.randint(10000, 30000), "description": "Advanced smart watch with health tracking."},
            {"id": random.randint(1, 1000), "name": "Gaming Console", "category": "electronics", "price": random.randint(25000, 55000), "description": "Latest generation gaming console for the ultimate gaming experience."},
            {"id": random.randint(1, 1000), "name": "4K Television", "category": "electronics", "price": random.randint(30000, 80000), "description": "Ultra HD 4K television with vibrant color display."},
            {"id": random.randint(1, 1000), "name": "Laptop", "category": "electronics", "price": random.randint(30000, 90000), "description": "Powerful and portable laptop suitable for professionals."},
            {"id": random.randint(1, 1000), "name": "Wireless Charger", "category": "electronics", "price": random.randint(1000, 7000), "description": "Fast charging wireless charger for mobile devices."},
            {"id": random.randint(1, 1000), "name": "Fitness Tracker", "category": "electronics", "price": random.randint(3000, 10000), "description": "Wearable fitness tracker to monitor your health metrics."},
            {"id": random.randint(1, 1000), "name": "Noise Cancelling Earbuds", "category": "electronics", "price": random.randint(4000, 12000), "description": "Compact earbuds with superior noise cancellation."},
            {"id": random.randint(1, 1000), "name": "E-Reader", "category": "electronics", "price": random.randint(6000, 18000), "description": "Lightweight e-reader perfect for avid readers."},
            {"id": random.randint(1, 1000), "name": "Drone", "category": "electronics", "price": random.randint(20000, 50000), "description": "High-performance drone with HD camera."},
            {"id": random.randint(1, 1000), "name": "Tablet Device", "category": "electronics", "price": random.randint(15000, 40000), "description": "Sleek tablet with high-resolution display and fast processing."},
            {"id": random.randint(1, 1000), "name": "Portable Speaker", "category": "electronics", "price": random.randint(5000, 15000), "description": "Portable Bluetooth speaker with exceptional sound quality."},
            {"id": random.randint(1, 1000), "name": "Robotic Vacuum", "category": "home appliances", "price": random.randint(8000, 25000), "description": "Smart robotic vacuum cleaner that simplifies cleaning."},
            {"id": random.randint(1, 1000), "name": "Air Purifier", "category": "home appliances", "price": random.randint(5000, 20000), "description": "Advanced air purifier to ensure a clean indoor environment."},
            {"id": random.randint(1, 1000), "name": "Smart Light Bulb", "category": "electronics", "price": random.randint(1000, 5000), "description": "Energy-efficient smart light bulb compatible with voice assistants."},
            {"id": random.randint(1, 1000), "name": "Graphic Drawing Tablet", "category": "electronics", "price": random.randint(5000, 15000), "description": "High-precision tablet for graphic designers and illustrators."},
            {"id": random.randint(1, 1000), "name": "Security Camera", "category": "home security", "price": random.randint(4000, 12000), "description": "Wi-Fi-enabled security camera with night vision."},
            {"id": random.randint(1, 1000), "name": "Handheld Gaming Console", "category": "electronics", "price": random.randint(8000, 20000), "description": "Compact handheld gaming console for on-the-go entertainment."},
            {"id": random.randint(1, 1000), "name": "Smart Thermostat", "category": "home appliances", "price": random.randint(7000, 18000), "description": "Programmable smart thermostat for optimal home temperature control."},
            {"id": random.randint(1, 1000), "name": "Cordless Hair Dryer", "category": "personal care", "price": random.randint(3000, 10000), "description": "Lightweight and powerful cordless hair dryer."},
            {"id": random.randint(1, 1000), "name": "Electric Kettle", "category": "kitchen appliances", "price": random.randint(2000, 7000), "description": "Fast-boiling electric kettle with temperature control."},
            {"id": random.randint(1, 1000), "name": "Smart Lock", "category": "home security", "price": random.randint(5000, 20000), "description": "Keyless entry smart lock with remote access via smartphone."},
            {"id": random.randint(1, 1000), "name": "Indoor Grill", "category": "kitchen appliances", "price": random.randint(3000, 10000), "description": "Smokeless indoor grill for healthy cooking."},
            {"id": random.randint(1, 1000), "name": "Bookshelf Speakers", "category": "electronics", "price": random.randint(6000, 18000), "description": "Compact bookshelf speakers with studio-quality sound."},
            {"id": random.randint(1, 1000), "name": "Humidifier", "category": "home appliances", "price": random.randint(2000, 8000), "description": "Ultrasonic cool mist humidifier for improved air quality."},
            {"id": random.randint(1, 1000), "name": "Multi-tool Pocket Knife", "category": "tools", "price": random.randint(1000, 4000), "description": "Versatile multi-tool pocket knife for everyday use."},
            {"id": random.randint(1, 1000), "name": "Yoga Mat", "category": "fitness", "price": random.randint(500, 3000), "description": "Eco-friendly and non-slip yoga mat for all types of yoga."},
            {"id": random.randint(1, 1000), "name": "Waterproof Backpack", "category": "outdoor gear", "price": random.randint(3000, 8000), "description": "Durable and waterproof backpack for hiking and travel."},
            {"id": random.randint(1, 1000), "name": "GoPro Camera", "category": "electronics", "price": random.randint(10000, 30000), "description": "Rugged GoPro camera for capturing extreme activities and sports."},
            {"id": random.randint(1, 1000), "name": "Resistance Bands Set", "category": "fitness", "price": random.randint(500, 2500), "description": "Set of resistance bands for strength training and fitness."},
            ]
        random.shuffle(products)
        data = products[0]
        obj = GeneratePerformance(1)
        mesg = {
            'Data':data ,
            'status' : True,
            'Average TIme' : obj.calculate_Response_Time(),
        }        
        return Response(mesg,status=status.HTTP_200_OK)

class GeneratePerformance():
    
    def __init__(self, userId) -> None:
         self.user = userId
    
    
    def calculate_Response_Time(self):
        
        average_duration = PurchaseOrder.objects.filter(vendor__user_id = self.user).annotate(
            response_time=ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=fields.DurationField()
            )
        ).aggregate(average_response_time=Avg('response_time'))
        
        return self.float_time_to_string(average_duration['average_response_time'].total_seconds() / 3600)


    def float_time_to_string(self,total_hours):
        hours = int(total_hours)  


        fractional_hours = total_hours - hours  
        minutes = fractional_hours * 60


        integral_minutes = int(minutes)  


        # fractional_minutes = minutes - integral_minutes
        # seconds = fractional_minutes * 60 

        # rounded_seconds = round(seconds)

        return f"{hours} hours, {integral_minutes} minutes"


#Vendor 

class Login(UserResponse,APIView):
    
    def post(self, request, *args, **kwargs):       
        data = request.data        
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email,password=password)
        
        if user:
            token = getRefreshToken(user)
            self._mesg.update({
                'access' : token.get('access'),
                'refresh' : token.get('refresh'),
                'user_id' : user.id , 
                'username' : user.name
            })
            return Response(self._mesg,status=status.HTTP_200_OK)
        
        self._mesg.update({
            'message' : 'Invalid User',
            'status' : False,             
        })
        return Response(self._mesg,status=status.HTTP_400_BAD_REQUEST)

class Get_Create_Vendors(UserResponse,generics.ListCreateAPIView):
    
    serializer_class = ModifyUserSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():       
            user = serializer.save()          
            tokens = getRefreshToken(user)
            self._mesg.update({
                'access' : tokens.get('access'),
                'refresh' : tokens.get('refresh') , 
                'user' : user.id,
                'username' : user.name
            })
            return Response(self._mesg,status=status.HTTP_201_CREATED)  

        
        errors = serializer.errors
        return Response(errors,status=status.HTTP_400_BAD_REQUEST)

class Update_Delete_Vendors(UserResponse,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [Auth_List_Create]
    authentication_classes = [JWTAuthentication]
    serializer_class = ModifyUserSerializer
    queryset = serializer_class.Meta.model.objects.all()
    
    def get_serializer_context(self):
        context = super(Update_Delete_Vendors, self).get_serializer_context()
        context['request'] = self.request
        return context
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['password'] = False
        return context
    
    def put(self, request, *args, **kwargs):
        user_Instance = self.get_object()
        serializer = self.serializer_class(instance=user_Instance,data=request.data,partial=True)
                
        if  serializer.is_valid():
            serializer.save()     

            self._mesg.update({
                'mesg' : f"{user_Instance.user} , Details Updated"   
            })      
            return Response(self._mesg,status=status.HTTP_200_OK)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)            
        except:
            self._mesg.update({
                'status' : False,
                'mesg' : "User Don't Exist",
            })
            return Response(self._mesg,status=status.HTTP_404_NOT_FOUND)
        user.delete()        
        self._mesg.update({
                'status' : True,
                'mesg' : "User Delete",
            }) 
        return Response(self._mesg,status=status.HTTP_204_NO_CONTENT)
  
#Purchase Orders

class Get_Create_Order(UserResponse,generics.ListCreateAPIView): 
    permission_classes = [Auth_List_Create]   
    authentication_classes = [JWTAuthentication]
    serializer_class = OrderSerializer
    
    

    
    def get_queryset(self):
        vendor = self.request.query_params.get('vendor')
        
        try:
            start = int(self.request.query_params.get('start', 0)) 
            end = int(self.request.query_params.get('end', 10))
        except:
            start = 0
            end = 10
        
        if not vendor:
            return self.serializer_class.Meta.model.objects.all()[start: end]
        
        if self.request.user.name != vendor:
            raise serializers.ValidationError(detail='Un Authorized Access')

        return self.serializer_class.Meta.model.objects.filter(vendor__user__name = vendor)[start:end]
         
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data,many=True)
        
        if serializer.data:
            self._mesg.update({
                'products': serializer.data,
                'status' : True,
            })
            return Response(self._mesg,status=status.HTTP_200_OK)
        
        self._mesg.update({
            'mesg' : "You Don't Have Any Orders Yet , Thanks ! ",
            'status' : False,
        })
        return Response(self._mesg,status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):       
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            self._mesg.update({
                'mesg' : f"Order Placed Your Order Id , {product.po_number}"
            })
            return Response(self._mesg,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors)
  
class Update_Delete_Order(UserResponse,generics.RetrieveUpdateDestroyAPIView):  
    permission_classes = [IsAuthenticated,amIOwner]
    serializer_class = OrderSerializer
    queryset = serializer_class.Meta.model.objects.all()
    

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            self._mesg.update({
                'status':True,
                'mesg' :  'Order Updated',
                'data' : serializer.data,
            })
            return Response(self._mesg,status=status.HTTP_200_OK)        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        
        try:
            instance = self.serializer_class.Meta.model.objects.get(po_number=kwargs.get('pk'))
        except:
            self._mesg.update({
                'mesg' : f"Order ID {kwargs.get('pk')} Not Found",
                'status':False
            })
            return Response(self._mesg,status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        self._mesg.update({
            'mesg' : f"Order ID {kwargs.get('pk')} Deleted",
            'status':True
        })
        return Response(self._mesg,status=status.HTTP_200_OK)
        
class AcknowledgeOrder(UserResponse,generics.UpdateAPIView):
    
    permission_classes = [IsAuthenticated,amIOwner]
    serializer_class = AcknowledgeOrderSerializer
    
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        try:
            return self.serializer_class.Meta.model.objects.get(po_number=pk)
        except:
            raise serializers.ValidationError(f"Order Id {pk} don't exist")
    
    def update(self, request, *args, **kwargs):
        
        order_type = self.request.query_params.get('type')
        instance = self.get_queryset()
        serializer = self.serializer_class(instance=instance,data=request.data,partial=True)
        if serializer.is_valid():
            
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
                            'mesg' : 'Approve , Purchase Order First !'
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
                    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


#Performance
    
class Get_Vendor_Performance(UserResponse,generics.RetrieveAPIView):
    
    serializer_class = VendorPerformanceSerializer
    
    def get_queryset(self):
        instance = self.serializer_class.Meta.model.objects.filter(user__id = self.kwargs.get('pk')).first()
        if not instance:
            self._mesg['mesg'] = "User Don't Exist "
            raise serializers.ValidationError(self._mesg)
        return instance
        
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.serializer_class(instance)
        self._mesg.update({
            'data' : serializer.data,
            'status' :True,
        })
        return Response(self._mesg,status=status.HTTP_200_OK)
        
    


       
        


    




    
    
    
    
    
    