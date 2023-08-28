from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
def display_topic(request):
    QSTO=Topic.objects.all()
    
    QSTO=Topic.objects.exclude(Topic_name='koko')
    QSTO=Topic.objects.filter(Topic_name='freefire')
    QSTO=Topic.objects.all()[1:3:1]


    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.all().order_by('name')
    QSWO=webpage.objects.all().order_by('-name')
    QSWO=webpage.objects.order_by(Length('name'))
    QSWO=webpage.objects.order_by(Length('Topic_name').desc())
    QSWO=webpage.objects.order_by(Length('name'))
    QSWO=webpage.objects.filter(Topic_name='koko')
    QSWO=webpage.objects.exclude(Topic_name='freefire')
    QSWO=webpage.objects.filter(name__startswith='l')
    QSWO=webpage.objects.filter(name__endswith='h')
    QSWO=webpage.objects.filter(name__contains='s')
    QSWO=webpage.objects.filter(name__regex=r'a')
   
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

   

def display_Access(request):
    QSAO=AccessRecords.objects.all()
    QSAO=AccessRecords.objects.filter(date__month='5')
    QSAO=AccessRecords.objects.filter(date__gt='2000-03-12')
    QSAO=AccessRecords.objects.filter(date__gte='1990-04-03')
    QSAO=AccessRecords.objects.filter(date__lt='1998-04-03')
    QSAO=AccessRecords.objects.filter(date__lte='2000-04-03')
    QSAO=AccessRecords.objects.filter(date__day='1')
    
    
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