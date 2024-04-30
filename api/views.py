from rest_framework import status,generics 
from rest_framework.response import Response
from .permissions import Auth_List_Create
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import  IsAuthenticated
from abc import ABC
from .serializer import *
from .utilis import  getRefreshToken

class UserResponse(ABC) :
    def __init__(self) -> None:
        self._mesg = {}

class Get_Create_Vendors(UserResponse,generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
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
            })
            return Response(self._mesg,status=status.HTTP_201_CREATED)  

        
        errors = serializer.errors

        return Response(errors,status=status.HTTP_400_BAD_REQUEST)

class Update_Delete_Vendors(UserResponse,generics.RetrieveUpdateDestroyAPIView):
    
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
            user = serializer.validated_data.get('user')
            self._mesg.update({
                'message' : f"{user.get('name')} , Details Updated"   
            })      
            return Response(self._mesg,status=status.HTTP_200_OK)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    


        
    
    
    
    
    
    