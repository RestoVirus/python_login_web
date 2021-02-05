from django import db
from django.db import models
from django.forms.widgets import Widget
from django import forms
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Customer(models.Model):
    customerEmail = models.EmailField(max_length=30,null=True)  
    customerLast = models.CharField(max_length=20,null=True)
    customerName = models.CharField(max_length=20,null=True)
   

