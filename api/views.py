from abc import ABC
from .serializer import *
from .utilis import  getRefreshToken
from rest_framework.views import APIView  
from .permissions import *
from rest_framework import status,generics 
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserResponse(ABC) :
    def __init__(self) -> None:
        self._mesg = {}

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
                'user' : user.id
            })
            return Response(self._mesg,status=status.HTTP_201_CREATED)  

        
        errors = serializer.errors

        return Response(errors,status=status.HTTP_400_BAD_REQUEST)

class Update_Delete_Vendors(UserResponse,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [amIOwner,IsAuthenticated]
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
                'message' : f"{user_Instance.user} , Details Updated"   
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
                'user' : user.id
            })
            return Response(self._mesg,status=status.HTTP_200_OK)
        
        self._mesg.update({
            'message' : 'Invalid User',
            'status' : False,             
        })
        return Response(self._mesg,status=status.HTTP_400_BAD_REQUEST)



    
    
    
    
    
    