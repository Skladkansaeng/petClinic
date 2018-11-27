from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.http import JsonResponse
from doctor.models import queue,vaccine,medical,appointment
from user.models import mypet
from createStaff.models import staff
from django.core import serializers

# from .models import Test
def doctor(request):
    # test = Test.objects.all()
    # jsonObj = json.dumps(queue.__dict__)
    # print(jsonObj)
    # serialized_obj = serializers.serialize('json', [ queue, ])
    # print(serialized_obj['fields'])
    return render(request, 'doctor.html')

    # return JsonResponse({"x": "doctor"})
    # ,{'first_name':test[0].first_name})

def getVaccine(req):
    obj = json.loads(req.body.decode('utf-8'))
    objQ =vaccine.objects.all()
    lst = []
    for pn in objQ:
        # print(pn.pet_name)
        # d = {}
        # d['petName']=pn.pet_name.name
        # d['type']=pn.pet_name.type
        # d['Weight']=pn.pet_weight
        # d['heartRate']=pn.pet_HeartRate
        # d['dehydration']=pn.pet_Dehydration
        # d['task']=pn.pet_want
        if obj['name'] == pn.pet_name.name and pn.pet_name.user.username == obj['username']:
            d = {'givenDate': pn.vaccine_date,'age':pn.pet_name.age,'immunization':pn.immunization,'vaccine':pn.vaccine,'dose':pn.dose,'nextDue':pn.next_due,'vet':pn.veterinarian}
            lst.append(d)
    return JsonResponse(lst, safe=False)

def getMedical(req):
    obj = json.loads(req.body.decode('utf-8'))
    objQ =medical.objects.all()
    lst = []
    for pn in objQ:
        # print(pn.pet_name)
        # d = {}
        # d['petName']=pn.pet_name.name
        # d['type']=pn.pet_name.type
        # d['Weight']=pn.pet_weight
        # d['heartRate']=pn.pet_HeartRate
        # d['dehydration']=pn.pet_Dehydration
        # d['task']=pn.pet_want
        if obj['name'] == pn.pet_name.name and pn.pet_name.user.username == obj['username']:
            d = {'date': pn.medical_date,'age':pn.pet_name.age,'symptom':pn.symptom,'medicine':pn.medicine,'notation':pn.monation,'vet':pn.veterinarian}
            lst.append(d)
    return JsonResponse(lst, safe=False)

def sendJson(req):
    objQ =queue.objects.all()
    lst = []
    for pn in objQ:
        # print(pn.pet_name)
        # d = {}
        # d['petName']=pn.pet_name.name
        # d['type']=pn.pet_name.type
        # d['Weight']=pn.pet_weight
        # d['heartRate']=pn.pet_HeartRate
        # d['dehydration']=pn.pet_Dehydration
        # d['task']=pn.pet_want
        d = {'username':pn.pet_name.user.username,'petName': pn.pet_name.name,'type':pn.pet_name.type,'age':pn.pet_name.age,'breed':pn.pet_name.breed,'weight':pn.pet_weight,'heartRate':pn.pet_HeartRate,'dehydration':pn.pet_Dehydration,'restRate':pn.pet_restRate,'task':pn.pet_want}
        lst.append(d)
        # print(lst)
    # jsongen = json.dumps(lst)
    # jsongen  = serializers.serialize('json', objQ)
    # print(jsongen[1])

    return JsonResponse(lst, safe=False)

def createVaccine(req):
    obj = json.loads(req.body.decode('utf-8'))
    for i in mypet.objects.all():
        if obj['pet_name'] == i.name:
            objM = i
            break
    db = vaccine(pet_name= i,vaccine_date=obj['vaccine_date'],vaccine_time=obj['vaccine_time'],immunization=obj['immunization'],vaccine=obj['vaccine'],dose=obj['dose'],next_due=obj['next_due'],veterinarian=obj['veterinarian'],age=i.age)
    db.save()
    dbApp = appointment(pet_name=i,next_due=obj['next_due'],time=obj['vaccine_time'],Description=obj['description'])
    print(dbApp)
    dbApp.save()
    for i in queue.objects.all():
        if obj['pet_name'] == i.pet_name.name:
            objM = i
            break
    objM.delete()
    return JsonResponse({"x": "doctor"})

def Makeappointment(req):
    obj = json.loads(req.body.decode('utf-8'))
    # print(obj)
    for i in mypet.objects.all():
        if obj['pet_name'] == i.name:
            objM = i
            break
    db = appointment(pet_name= i,next_due=obj['next_due'],time = obj['time'],Description=obj['Description'],username = obj['username'])
    # print(db)
    db.save()
    return JsonResponse({"x": "doctor"})

def createMedical(req):
    obj = json.loads(req.body.decode('utf-8'))
    for i in mypet.objects.all():
        if obj['pet_name'] == i.name:
            objM = i
            break
    db = medical(pet_name =i,medical_date=obj['medical_date'],symptom=obj['symptom'],medicine=obj['medicine'],monation=obj['monation'],veterinarian=obj['veterinarian'],age=i.age)
    db.save()
    for i in queue.objects.all():
        if obj['pet_name'] == i.pet_name.name:
            objM = i
            break
    objM.delete()
    return JsonResponse({"x": "doctor"})

def fonTest(req,pk):
    obj = staff.objects.get(pk=pk)
    context={"name": obj.name,"surname": obj.surname}
    # context={"name":'d',"surname":'p'}
    return render(req,'doctor.html',context)
