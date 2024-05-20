from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class UserModel(AbstractUser):
    profile_img = models.ImageField(upload_to="profile_image",blank=True, null=True)
    mobile_number = models.CharField(max_length=10) 
    
   


class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_img = models.ImageField(upload_to="service_img")
    service_diss= models.TextField(max_length=500)

    def __str__(self):
        return self.service_name


class ServiceMan(models.Model):
    serviceId= models.ForeignKey(Services, on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    experience = models.CharField(max_length=10, blank=True)
    profile_img= models.ImageField(upload_to="serviceman_pro")

    def __str__(self):
        return self.name

class Orders(models.Model):
    serviceId = models.ForeignKey(Services, on_delete=models.CASCADE, blank=True,null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    order_data= models.DateField(auto_created=True,auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.user.username
