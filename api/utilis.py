import datetime
import random
from abc import ABC , abstractmethod
from rest_framework_simplejwt.tokens import RefreshToken 



def getRefreshToken(user):
    token = RefreshToken.for_user(user)
        
    return {
        'refresh' : str(token),
        'access' : str(token.access_token)
    }

def generate_unique_Id(username):
    now = datetime.datetime.now()
    timestamp = now.strftime("%y%m%d%H%M%S%f")[:-3]
    username_prefix = username.split(' ')[0] 
    number = random.randint(1, 999999)
    
    return f"{username_prefix}-{timestamp}-{number:06}"

class Float_Time_To_String():
    
    def float_time_to_string(self,total_hours):
        hours = int(total_hours)  
        fractional_hours = total_hours - hours  
        minutes = fractional_hours * 60
        integral_minutes = int(minutes)  
        return f"{hours} hours, {integral_minutes} minutes"

class UserResponse() :
    
    def __init__(self) -> None:
        self._mesg = {}

    
    def custom_response(self , status :bool, mesg:str = None ,**kwarg ) -> dict:
        message = {
            'status':status,
            'mesg' : mesg 
        }
        if not mesg :
            message.pop('mesg')
            
        message.update(kwarg)            
        return message

class OrderHandler(ABC) :
    
    @abstractmethod
    def validate(self,instance):
        pass
    
    @abstractmethod
    def handle(self,instance):
        pass
    
    @abstractmethod
    def send_signal(self,instance):
        pass

class Calculate(ABC):
    
    def __init__(self,instance) -> None:
        self._vendor = instance
    
    @abstractmethod
    def calculate(self):        
        pass
    