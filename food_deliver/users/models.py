from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from phone_field import PhoneField
class Users(AbstractUser):
    Role_CHOICES = [
    ('s', 'seller'),
    ('c', 'customer'),
    ('d','delivery'),   
]
    username = models.CharField(max_length=50,null=True,blank=True)
    phone = PhoneField(help_text='Contact phone number')
    image = models.ImageField(upload_to='images',blank=True)
    role = models.CharField(max_length=1,choices=Role_CHOICES,default=Role_CHOICES[1])
    email = models.EmailField(unique=True)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username']

    