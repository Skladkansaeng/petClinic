from django.shortcuts import render
from user.models import *
from doctor.models import *
import json
from django.http import JsonResponse
# Create your views here.
def userpage(request):
    return render(request, 'user.html')

def userData(request,pk):
    obj = user.objects.get(pk=pk)
    pet = mypet.objects.filter(user= obj)
    listPet = []
    for p in pet:
        d = {"petName":p.name , "type":p.type , "birthDate":p.birthDate , "age":p.age , "breed":p.breed , "sick":p.sickness}
        listPet.append(d)
    return JsonResponse(listPet, safe=False)

def appData(request,pk):
    obj = user.objects.get(pk=pk)
    pet = mypet.objects.filter(user = obj)
    apm = []
    for p in pet:
        app = appointment.objects.filter(pet_name = p)
        for a in app:
            d = {"pet":a.pet_name.name , "date":a.next_due , "time":a.time , "description":a.Description}
            apm.append(d)
    print(apm)
    return JsonResponse(apm, safe=False)


def fonTest(req,pk):
    obj = user.objects.get(pk=pk)
    # app = appointment.objects.get(pet_name = obj.)
    context={"name": obj.name,"surname": obj.surname,"email":obj.email,"tel":obj.tel,"pk":pk}
    # context={"name":'d',"surname":'p'}
    return render(req,'user.html',context)

def editProfile(request,pk):
    obj = json.loads(request.body.decode('utf-8'))
    profile = user.objects.get(pk = pk)
    profile.name = obj['name']
    profile.surname = obj['surname']
    profile.tel =  obj['tel']
    profile.email = obj['email']
    profile.save()
    a={'oak':2}
    return JsonResponse(a)
