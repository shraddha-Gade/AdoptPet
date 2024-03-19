from django.db import models
from sign_up.models import CustomUser

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
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE , default='',null = True)


    
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
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE ,default=3,null = True)


    
