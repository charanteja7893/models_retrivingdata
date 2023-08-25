from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
def display_Access(request):
    QSAO=AccessRecords.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_Access.html',d)

def insert_topic(request):
    tn=input('Enter topic name:')
    to=Topic.objects.get_or_create(topic_name=topic_name)[0]
    to.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)
def insert_webpage(request):
    tn=input('enter topic_name')
    to=Topic.objects.get(topic_name=tn)
    na=input('enter name')
    ur=input('enter url')
    wo=webpage.objects.get_or_create(topic_name=to,name=name,url=url)[0]
    wo.save()
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
def insert_Access(request):
    pk=input('Enter a number:')
    d=input('Enter date:')
    a=input('Enter Author name:')
    wo=webpage.objects.get(pk=pk)
    ao=Access_Records.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    QSAO=Access_Records.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_Access.html',d)