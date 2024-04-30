from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractUser
from .utilis import generate_unique_Id

    
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_kwargs):        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email,password,**extra_fields)

class User(AbstractUser):

    class Meta:
        db_table = "users"
        
    email = models.EmailField(unique=True)
    name = models.CharField(verbose_name="Name",max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.name
     
class Vendor(models.Model):
    
    class Meta:
        db_table = "vendor"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor')
    contact_details = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True)
    address = models.TextField()   
    on_time_delivery_rate = models.FloatField(blank=True,null=True)
    quality_rating_avg = models.FloatField(blank=True,null=True)
    average_response_time = models.FloatField(blank=True,null=True)
    fulfillment_rate = models.FloatField(blank=True,null=True)
    
    
    def save(self,*args,**kwargs):
        if not self.vendor_code :
            self.vendor_code = generate_unique_Id(self.user.name)      
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.name



    
    

