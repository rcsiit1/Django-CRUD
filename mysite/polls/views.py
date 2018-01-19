from django.shortcuts import render
from django.http import HttpResponse
from .models import info
from django.urls import reverse

def index(request):
    all_info= info.objects.all()
    context={'all_info': all_info}
    return render(request,'polls/index.html',context)

def create(request):
    obj = info.objects.get(id=request.GET['id'])
    obj.firstname = request.GET['firstname']
    obj.lastname= request.GET['lastname']
    obj.designation = request.GET['designation']
    obj.department = request.GET['department']
    obj.date= request.GET['date']
    obj.save()
    all_info = info.objects.all()
    return render(request, 'polls/index.html',{'all_info':all_info})

def store(request):
    obj = info()
    obj.id=request.GET['id']
    obj.firstname = request.GET['firstname']
    obj.lastname = request.GET['lastname']
    obj.designation = request.GET['designation']
    obj.department = request.GET['department']
    obj.date = request.GET['date']
    obj.save()
    all_info= info.objects.all()
    return render(request, 'polls/index.html', {'all_info': all_info})

def insert(request):
    reco= info.objects.last()
    record = reco.id + 1
    return render(request, 'polls/insert.html',{'record':record})


def update(request):
    if 'update' in request.GET:
        obj_info = info.objects.get(id=request.GET['id'])
        return render(request, 'polls/update.html',{'obj_info': obj_info})

    elif 'delete' in request.GET:
        delete_rec = info.objects.filter(id=request.GET['id'])
        delete_rec.delete()
        all_info = info.objects.all()
        return render(request, 'polls/index.html', {'all_info': all_info})
