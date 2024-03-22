from django.db import models
from sign_up.models import CustomUser
from django.contrib.auth import get_user_model




# Create your models here.
class Cat(models.Model):

    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    breed = models.CharField(max_length = 100 , blank = True , null = True)
    age = models.IntegerField()
    vaccinated = models.BooleanField()
    city = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'cat_images/')
    is_available = models.BooleanField(default=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cats_added', default = 3)
    adopted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cats_adopted' , default = 3)
    
    
    
class Dog(models.Model):

    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    breed = models.CharField(max_length = 100 , blank = True , null = True)
    age = models.IntegerField()
    vaccinated = models.BooleanField()
    city = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'dog_images/')
    is_available = models.BooleanField(default=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dogs_added', default = 3)
    adopted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dogs_adopted' , default = 3)
    

   

    
