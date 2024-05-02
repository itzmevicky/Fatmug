import datetime
import random

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

