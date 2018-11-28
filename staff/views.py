from django.shortcuts import render
import json
from django.http import JsonResponse
from user.models import user
from createStaff.models import staff

# # Create your views here.
# def staff(request):
#     return render(request, 'staff.html')

def createUser(request):
    print('test')
    obj = json.loads(request.body.decode('utf-8'))
    print(obj)
    db = user(name = obj['firstname'] , surname = obj['lastname'] , tel =obj['tel'] ,
    email= obj['email'] , username= obj['username'], password= obj['password'] )
    db.save()
    return JsonResponse({"w": "wr"})

def get_userInfo(request):
    objUser = user.objects.all()
    obj = json.loads(request.body.decode('utf-8'))
    print(obj)
    lst = []
    findUser = obj['str_input']
    for pn in objUser:
        if pn.name[:len(findUser)].lower() == findUser :    
                d={"value": pn.name,"link": pn.pk}
                lst.append(d)

    return JsonResponse(lst, safe=False)

def fonTest(req,pk):
    obj = staff.objects.get(pk=pk)
    context={"name": obj.name,"surname": obj.surname}
    # context={"name":'d',"surname":'p'}
    return render(req,'staff.html',context)