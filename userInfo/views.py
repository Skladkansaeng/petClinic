from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.http import JsonResponse
from doctor.models import queue,vaccine,medical,appointment
from user.models import mypet,user
from createStaff.models import staff
from django.core import serializers
from dateutil.parser import parse
import time
from datetime import datetime
# Create your views here.

def userInfo(res,pk):
    obj = user.objects.get(pk=pk)
    context={"name": obj.name,"surname": obj.surname,"username": obj.username,"tel":obj.tel,"email":obj.email}
    return render(res, 'userInfo.html',context)

def getDataJson(res):
  
    lst = []
    obj = json.loads(res.body.decode('utf-8'))
    # objUser = mypet.objects.filter(user = obj['str_input'])
 
    # print(objUser)
    for i in mypet.objects.all():
        if i.user.username == obj['str_input']:
            d = {'petName':i.name,'type':i.type,'birthDate':i.birthDate,'age':i.age,'breed':i.breed,'sick':i.sickness}
            lst.append(d)
    return JsonResponse(lst, safe=False)

def newPet(res):
    objQ = json.loads(res.body.decode('utf-8'))
    objUser = user.objects.all()
    currentTime = datetime.now()
    day = int(( int(round( currentTime.timestamp()* 1000 )) - int(round( parse(objQ['birthDate']).timestamp()* 1000 )) )/1000/60/60/24)
    week = int(day/7)
    mont = int(week/4)
    year = int(mont/12)
    pet_age = ""
    if year >0:
        pet_age = str(year)+"y"+str(mont%12)+"m"
    elif mont >0:
        pet_age = str(mont%12)+"m"+str(week%4)+"w"
    elif week > 0:
        pet_age = str(week)+"w"
    elif week == 0:
        pet_age = str(day)+"d"

    for pn in user.objects.all():
        if pn.username == objQ['username']:
            objUser = pn
            break
    for i in mypet.objects.all():
        if i.user.username == objUser.username:            
            if objQ['name'] == i.name and objQ['type'] == i.type:
                return JsonResponse({"res": "cant"},safe=False)
    save = mypet(user =  objUser,name= objQ['name'] ,type = objQ['type'],birthDate=parse(objQ['birthDate']),age=pet_age,breed=objQ['breed'],sickness=objQ['sickness'])
    save.save()
    return JsonResponse({"res": "can"},safe=False)

def get_staffInfo(request):
    objUser = staff.objects.all()
    obj = json.loads(request.body.decode('utf-8'))
    print(obj)
    lst = []
    findUser = obj['str_input']
    for pn in objUser:
        if pn.name[:len(findUser)].lower() == findUser  and pn.status == "Doctor":    
                d={"value": pn.name+ " "+ pn.surname,"link": pn.pk}
                lst.append(d)

    return JsonResponse(lst, safe=False)

def makeQueue(res):
    status = True
    objQ = json.loads(res.body.decode('utf-8'))
    objpet = queue.objects.all()
    for j in objpet:
        if j.pet_name.user.username == objQ['username']:                
            if objQ['pet_name'] == j.pet_name.name:
                print( j.pet_want == objQ['pet_want'])
                if j.pet_want == objQ['pet_want']:
                    status = False
                    return JsonResponse({"res": "Have"},safe=False)
                
    for i in mypet.objects.all():
        if i.user.username == objQ['username']: 
            if objQ['pet_name'] == i.name:
                petname = i
                break
    if status:
        save = queue(pet_name=petname,pet_weight=objQ['pet_weight'],pet_HeartRate=objQ['pet_heartRate'],pet_restRate=objQ['pet_restRate'],pet_Dehydration=objQ['pet_Dehydration'],pet_want=objQ['pet_want'],veterinarian=objQ['veterinarian'],description=objQ['description'])
        save.save()
        return JsonResponse({"res": "suc"},safe=False)

        

