# Global Imports

import random 

from .models import *
from .utilis import *
from .signals import *
from .serializer import *
from .permissions import *

from rest_framework.views import APIView  
from rest_framework import status,generics 
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class GenerateRandomProducts(APIView , UserResponse):
    
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
        rep = self.custom_response(status=True,data=data)
        return Response(rep,status=status.HTTP_200_OK)


#Vendor 

class Login(UserResponse,APIView):
    
    def post(self, request, *args, **kwargs):       
        data = request.data        
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email,password=password)        
        if user:
            token = getRefreshToken(user)            
            
            data = {
                'user_id' : user.id , 
                'username' : user.name
            }
            
            data.update(token)            
            rep = self.custom_response(status=True , **data )            
            return Response(rep,status=status.HTTP_200_OK)        
        
        rep = self.custom_response(status=False,mesg="Invalid User")
        return Response(rep,status=status.HTTP_400_BAD_REQUEST)

class List_Create_Vendors(generics.ListCreateAPIView,UserResponse):
    
    serializer_class = ModifyUserSerializer
    queryset = serializer_class.Meta.model.objects.all()
    

    
    # def get_object(self):
    #     pk = self.request.query_params.get('userId') 
        
    #     if not pk:            
    #         return None
            
    #     try:
    #         instance = self.serializer_class.Meta.model.objects.get(id=pk)
    #     except:
    #         raise serializers.ValidationError("User Don't Exist")
        
    #     return instance
    
    # def get(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         if instance:                
    #             serializer = self.serializer_class(instance)   
    #         else:
    #             instance =  self.get_queryset()
    #             serializer = self.serializer_class(instance,many=True)
                    
    #     except ValidationError as e:            
    #         rep = self.custom_response(status=False,mesg=e.args[0])
    #         return Response(rep,status=status.HTTP_400_BAD_REQUEST)
        
    #     rep = self.custom_response(status=True,data=serializer.data)
    #     return Response(rep,status=status.HTTP_200_OK)
        
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():       
            user = serializer.save()          
            token = getRefreshToken(user)
            data = {
                'user_id' : user.id , 
                'username' : user.name
            }
            
            data.update(token)            
            rep = self.custom_response(status=True , **data )            
            return Response(rep,status=status.HTTP_200_OK)        
        
        rep = self.custom_response(status=False,mesg="Invalid User",data=serializer.error_messages)
        return Response(rep,status=status.HTTP_400_BAD_REQUEST)

class Get_Update_Delete_Vendors(UserResponse,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [Auth_List_Create]
    authentication_classes = [JWTAuthentication]
    serializer_class = ModifyUserSerializer
    queryset = serializer_class.Meta.model.objects.all()
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        try:
            instance = self.serializer_class.Meta.model.objects.get(user__id=pk)
        except Exception as ex:
            raise serializers.ValidationError("User Doesn't Exist")
        return instance
        
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        context['password'] = False
        return context
    
    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance:                
                serializer = self.serializer_class(instance)   
            else:                
                serializer = self.queryset()
                    
        except ValidationError as e:            
            rep = self.custom_response(status=False,mesg=e.args[0])
            return Response(rep,status=status.HTTP_400_BAD_REQUEST)
        
        rep = self.custom_response(status=True,data=serializer.data)
        return Response(rep,status=status.HTTP_200_OK)
        
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance,data=request.data,partial=True)
                        
        if  serializer.is_valid():
            serializer.save()     
            rep = self.custom_response(status=True,mesg=f"{instance.user} , Details Updated" )
            return Response(rep,status=status.HTTP_200_OK)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, *args, **kwargs):        
        user = self.get_queryset()  
        user.user.delete()  
        rep = self.custom_response(status=True,mesg="User Delete")
        return Response(rep,status=status.HTTP_204_NO_CONTENT)

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
            rep = self.custom_response(status=True,products=serializer.data)
            return Response(rep,status=status.HTTP_200_OK)        
        rep = self.custom_response(status=False,mesg="You Don't Have Any Orders Yet , Thanks !")
        
        return Response(rep,status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):       
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            rep = self.custom_response(status=True,mesg=f"Order Placed Your Order Id , {product.po_number}")
            return Response(rep,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
class Update_Delete_Order(UserResponse,generics.RetrieveUpdateDestroyAPIView):  
    
    permission_classes = [IsAuthenticated,amIOwner]
    serializer_class = OrderSerializer

    def get_object(self):
        pk =  self.kwargs.get('pk')      
        instance = None  
        try:
            instance = self.serializer_class.Meta.model.objects.get(po_number=pk)
        except:
            return False , instance 
        return True , instance 
    
    def get(self, request, *args, **kwargs):
        result ,instance  = self.get_object()
        if result:
            serializer = self.serializer_class(instance)
            rep = self.custom_response(status=result,data=serializer.data)
            return Response(rep,status=status.HTTP_200_OK)        
        rep = self.custom_response(status=result,mesg=f"Order Id {self.kwargs.get('pk')} doesn't exist")
        return Response(rep,status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        result ,instance  = self.get_object()
        
        if result:
            serializer = self.serializer_class(instance=instance,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()            
                rep =self.custom_response(status=True,mesg='Order Updated',data=serializer.data)            
                return Response(rep,status=status.HTTP_200_OK)  
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                    
        rep = self.custom_response(status=result,mesg=f"Order ID {self.kwargs.get('pk')} Not Found")
        return Response(rep,status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, *args, **kwargs):
        
        result ,instance  = self.get_object()
                
        if result:
            instance.delete()
            rep = self.custom_response(status=True,mesg=f"Order ID {self.kwargs.get('pk')} Deleted")
            return Response(rep,status=status.HTTP_200_OK)        
        rep = self.custom_response(status=False,mesg=f"Order ID {self.kwargs.get('pk')} Not Found")
        return Response(rep,status=status.HTTP_404_NOT_FOUND)

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
        
        instance = self.get_queryset()
        serializer = self.serializer_class(instance=instance,data=request.data,partial=True)
        order_type = self.request.query_params.get('type')
        if serializer.is_valid(raise_exception=True): 
                                   
            if order_type == "order_approved":
                handler = Handle_Order_Approve()
                result , message = handler.handle(instance)
                
                if result:       
                    handler.send_signal(instance)             
                    response = self.custom_response(status=result,mesg=message)                    
                    return Response(response,status=status.HTTP_200_OK)
                                
                response = self.custom_response(result,message)
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
            
            elif order_type == "order_delivered":
                handler = Handle_Order_Delivered()
                result , message = handler.handle(instance)
                
                if result:
                    handler.send_signal(instance)
                    response = self.custom_response(status=result,mesg=message) 
                    return Response(response,status=status.HTTP_200_OK)
                
                response = self.custom_response(result,message)
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
                    
            elif order_type == "order_cancel":
                handler = Handle_Order_Cancel()
                result , message = handler.handle(instance)
                if result:
                    handler.send_signal(instance)
                    response = self.custom_response(status=result,mesg=message) 
                    return Response(response,status=status.HTTP_200_OK)
                
                response = self.custom_response(status=result,mesg=message) 
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
            
            elif order_type == "order_rate":                
                po_rating = self.request.query_params.get('rating')
                handler = Handle_Order_Rate()
                result , message = handler.handle(instance,rating=po_rating)
                
                if result:
                    handler.send_signal(instance)
                    response = self.custom_response(status=result,mesg=message,data=serializer.data) 
                    return Response(response,status=status.HTTP_200_OK)
                
                response = self.custom_response(status=result,mesg=message) 
                return Response(response,status=status.HTTP_400_BAD_REQUEST)

            else:
                rep = self.custom_response(status=False,mesg="order_type must pass")
                return Response(rep,status=status.HTTP_404_NOT_FOUND)

#Performance

class Get_Vendor_Performance(UserResponse,generics.RetrieveAPIView):
    
    serializer_class = VendorPerformanceSerializer
    
    def get_object(self):
        instance = self.serializer_class.Meta.model.objects.filter(user__id = self.kwargs.get('pk')).first()
        if instance:
            return instance
        raise serializers.ValidationError("User Don't Exist")
            
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)        
        rep = self.custom_response(status=True,data=serializer.data)
        return Response(rep,status=status.HTTP_200_OK)


class Handle_Order_Approve(OrderHandler) :
    
    def validate(self, instance):
        if instance.acknowledgment_date:
            return False, 'This order has already been acknowledged.'
        return True , None
            
    def handle(self, instance):
        validate = self.validate(instance)
        if validate[0]:
            instance.acknowledgment_date = timezone.now()
            instance.save()
            return True, 'Order acknowledged successfully.'
        return validate
    
    def send_signal(self, instance):
        post_save_signal.send(sender=instance.__class__ , instance=instance ,type="order_approved")

class Handle_Order_Delivered(OrderHandler):
    
    def validate(self, instance):
        if not instance.acknowledgment_date:
            return False , 'Approve , Purchase Order First'
        
        if instance.status == 'canceled':
            return False , 'Invalid , Order Already Canceled'
        
        if instance.status == 'completed':
            return False , 'Invalid , Order Already Delivered'
                
        return True , None
    
    def handle(self, instance):
        validate = self.validate(instance)
        if validate[0]:
            instance.status = 'completed'
            instance.actual_delivered_date = timezone.now()
            instance.save()
            return True, 'Order Delivered successfully.'
        return validate
    
    def send_signal(self, instance):
        post_save_signal.send(sender=instance.__class__ , instance=instance ,type="order_delivered")
        
class Handle_Order_Cancel(OrderHandler):
    
    def validate(self, instance):
        if instance.status == 'canceled':
            return False , 'Invalid , Order Already Canceled'
        return True , None
    
    def handle(self, instance):
        validate = self.validate(instance)
        if validate[0]:
            instance.status = 'canceled'
            instance.save()
            return True, 'Order Canceled successfully'
        
        return validate
    
    def send_signal(self, instance):
        post_save_signal.send(sender=instance.__class__ , instance=instance ,type="order_cancel")

class Handle_Order_Rate(OrderHandler):
    
    def validate(self, instance):
        if instance.quality_rating:
            return False , "Rating Already Provided"
        
        if instance.status != 'completed':
            return False , "Invalid , already product canceled , unable to rate"

        return True , None

    def handle(self, instance,**kwarg):        
        validate = self.validate(instance)
        if validate[0]:
            instance.quality_rating = kwarg.get('rating')
            instance.save()
            return True, 'Product Rating Updated'
        return validate
        
    def send_signal(self, instance):
        post_save_signal.send(sender=instance.__class__ , instance=instance ,type="order_rate")
       
        


    




    
    
    
    
    
    