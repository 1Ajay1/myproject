"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from distutils.log import debug
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from mywebsite import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contact/',views.contact1,name='contact'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('signup/',views.signup,name='signup'),
    path('joinus/',views.joinus,name='joinus'),
    path('tutorials/',views.tutotial,name='tutorial'),
    path('javaScripts/',views.javaScriptTutotial,name='javascript'),
    path('courses/',views.courses,name='courses'),
    path('forStoredata/',views.login,name='forStoredata'),
    path('forStoredata1/',views.forStoredata1,name='forStoredata1'),
    path('oracleNotes/',views.oracleNote,name='oracleNote'),
    path('interviewQuestion/',views.interviewQuestion,name='interviewQuestion'),
    path('pythonCoding/',views.pythonCode,name='pythonCoding'),
    path('javaCoding/',views.javaCode,name='javaCoding'),
]

if settings.DEBUG:
    urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)