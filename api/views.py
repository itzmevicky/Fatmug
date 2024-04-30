from rest_framework import status,generics 
from rest_framework.response import Response
from abc import ABC
from .serializer import UserSerializer

from .utilis import  getRefreshToken

class UserResponse(ABC) :
    def __init__(self) -> None:
        self._mesg = {}

class Get_Create_Vendors(UserResponse,generics.ListCreateAPIView):
    
    serializer_class = UserSerializer
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
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

