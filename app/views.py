from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'dhoni.html',d)

def insert_Webpage(request):
    tn=input('enter the topic name')
    n=input('enter the name')
    u=input('enter the url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('Webpage data is inserted sucessfully')
def insert_Accessdata(request):
    tn=input('enter the topic name')
    n=input('enter the name')
    u=input('enter the url')
    a=input('enter the author name')
    d=input('enter the date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    AO.save()
    return HttpResponse('AccessRecord data is sucessfully')


