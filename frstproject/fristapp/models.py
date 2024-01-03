from django.db import models
######employee
# # Create your models here.
# class Employee(models.Model):
#     name =models.CharField(max_length=100)
#     domain =models.CharField(max_length=100)
#     company =models.CharField(max_length=100)
    
#########movie
# class Movie(models.Model):
#     moviename =models.CharField(max_length=100)
#     budget =models.CharField(max_length=100)
#     director =models.CharField(max_length=100)
#     heroname=models.CharField(max_length=100)

########login,logout,homepage
from django.db import models

class facebook(models.Model):
    username = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confrmpassword = models.CharField(max_length=100)
   

  



        