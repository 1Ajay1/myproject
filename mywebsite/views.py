import email
from contact.models import javaScript, sign_up,join_us,contact,python,questionAnswer,pythonCoding,javaCoding
from xml.dom.minidom import Document
from django.shortcuts import render


def index(request):
    return render (request,'index.html' )

def contact1(request):
    return render(request,'contact.html')

def contact_us(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        quary=request.POST.get('quary')
        member=request.POST.get("flexRadioDefault")
        print(name,email,desc,quary,member)
        if member=='YES':
            m=contact(email=email,name=name,quary=quary,desc=desc,member='YES')
            m.save()
            return render (request,'index.html' )
        else:
            s=contact(email=email,name=name,quary=quary,desc=desc,member='NO')
            s.save()
            return render (request,'index.html' )
    else:
        return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pwd1=request.POST.get('password1')
        pwd2=request.POST.get('password2')
        if pwd1==pwd2:
            sign=sign_up(email=email,password=pwd1)
            sign.save()
            return render (request,'index.html' )
        else:
            return render (request,'contact.html' )
    else:
        return render (request,'index.html' )

def joinus(request):
    if request.method=='POST':
        name=request.POST.get("name")
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        resume=request.POST.get("resume")
        m=join_us(username=name,phone_number=phone,email=email,resume=resume)
        m.save()
        return render (request,'contact.html' )
        
    else:
        return render (request,'contact.html' )
def tutotial(request):
    Python_data=python.objects.all()
    return render(request,"Toturialcomingsoon.html",{"Python_data":Python_data})

def javaScriptTutotial(request):
    Javascript_data=javaScript.objects.all()
    return render(request,"javaScript.html",{"Javascript_data":Javascript_data})


def courses(request):
    return render(request,'Courses.html')

def login(request):
    if request.method=='POST':
        password=request.POST.get("password")
        username=request.POST.get('username')
        if username=='mywebsite' and password=='mywebsite':
            return render (request,'forStoredata.html' )
        else:
            print("ID and password is wrong")
            return render (request,'index.html' )
        
    else:
        return render ("Something went wrong" )

def forStoredata1(request):
    if request.method=='POST':
        topic_name=request.POST.get("topic_name")
        topic_description=request.POST.get('topic_description')
        print("hello")
        m=python(heading=topic_name,description=topic_description)
        m.save()
        print("hello")
        return render (request,'forStoredata.html' )
        
    else:
        return render ("Something went wrong" )

def interviewQuestion(request):
    question_answer=questionAnswer.objects.all()
    return render(request,"interviewQuestion.html",{"questionAnswer":question_answer})

def pythonCode(request):
    question_answer=pythonCoding.objects.all()
    return render(request,"pythonCoding.html",{"questionAnswer":question_answer})

def javaCode(request):
    question_answer=javaCoding.objects.all()
    return render(request,"javaCoding.html",{"questionAnswer":question_answer})


def oracleNote(request):
    return render(request,"oracleNotes.html")

