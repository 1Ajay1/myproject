from ctypes.wintypes import SIZE
from email.policy import default
from operator import mod
from xml.dom.minidom import Document
from django.db import models

# Create your models here.
class sign_up(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=25)
    def __str__(self):
        return self.email
class join_us(models.Model):
    username=models.CharField(max_length=50)
    phone_number =models.CharField(max_length=12)
    email=models.CharField(max_length=32)
    resume = models.FileField(upload_to ='media/',max_length=250,null=True,default=None)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

class contact(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=30)
    quary=models.CharField(max_length=60)
    desc=models.CharField(max_length=250)
    member=models.CharField(max_length=5)
    def __str__(self):
        return self.email

class python(models.Model):
    heading=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.heading

class javaScript(models.Model):
    heading=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.heading

class questionAnswer(models.Model):
    Question=models.CharField(max_length=500)
    Solution=models.TextField()
    '''answer1=models.TextField()
    answer2=models.TextField()
    answer3=models.TextField()'''

    def __str__(self):
        return self.Question

class pythonCoding(models.Model):
    Question=models.TextField()
    Solution=models.TextField()
    answer1=models.TextField()
    answer2=models.TextField()
    answer3=models.TextField()

    def __str__(self):
        return self.Question
    
class javaCoding(models.Model):
    Question=models.TextField()
    Solution=models.TextField()
    answer1=models.TextField()
    answer2=models.TextField()
    answer3=models.TextField()

    def __str__(self):
        return self.Question
    