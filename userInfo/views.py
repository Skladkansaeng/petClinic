from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.http import JsonResponse
from doctor.models import queue,vaccine,medical,appointment
from user.models import mypet,user
from django.core import serializers
from dateutil.parser import parse
# Create your views here.

def userInfo(res):
    return render(res, 'userInfo.html')

def getDataJson(res):
    objQ = mypet.objects.all()    
    lst = []
    for i in objQ:
        d = {'petName':i.name,'type':i.type,'birthDate':i.birthDate,'age':i.age,'breed':i.breed,'sick':i.sickness}
        lst.append(d)
    return JsonResponse(lst, safe=False)

def newPet(res):
    objQ = json.loads(res.body.decode('utf-8'))
    print(objQ)
    for i in mypet.objects.all():
        if objQ['name'] == i.name and objQ['type'] == i.type:
            return JsonResponse({"res": "cant"},safe=False)
    save = mypet(user = user.objects.get() ,name= objQ['name'] ,type = objQ['type'],birthDate=parse(objQ['birthDate']),age=objQ['age'],breed=objQ['breed'],sickness=objQ['sickness'])
    save.save()
    return JsonResponse({"res": "can"},safe=False)

def makeQueue(res):
    status = True
    objQ = json.loads(res.body.decode('utf-8'))
    objpet = queue.objects.all()
    for j in objpet:
        if objQ['pet_name'] == j.pet_name.name:
            status = False
            return JsonResponse({"res": "Have"},safe=False)
    for i in mypet.objects.all():
        if objQ['pet_name'] == i.name:
            petname = i
            break
    if status:
        print(objQ)
        save = queue(pet_name=petname,pet_weight=objQ['pet_weight'],pet_HeartRate=objQ['pet_heartRate'],pet_restRate=objQ['pet_restRate'],pet_Dehydration=objQ['pet_Dehydration'],pet_want=objQ['pet_want'],veterinarian=objQ['veterinarian'],description=objQ['description'])
        save.save()
        return JsonResponse({"res": "suc"},safe=False)

        

