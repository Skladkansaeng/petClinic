from django.shortcuts import render
from user.models import *
from doctor.models import *
import json
from django.http import JsonResponse
# Create your views here.
def userpage(request):
    return render(request, 'user.html')





def fonTest(req,pk):
    obj = user.objects.get(pk=pk)

    pet = mypet.objects.filter(user= obj)
    listPet = []
    for p in pet:
        d = {"petName":p.name , "type":p.type , "birthDate":p.birthDate , "age":p.age , "breed":p.breed , "sick":p.sickness}
        listPet.append(d)
    print(listPet)
    # app = appointment.objects.get(pet_name = obj.)
    context={"name": obj.name,"surname": obj.surname,"email":obj.email,"tel":obj.tel,"pk":pk,"listPet":listPet}




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
