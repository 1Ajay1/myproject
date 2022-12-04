from distutils.log import debug
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from mywebsite import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('contact/',views.contact,name='contact')
]