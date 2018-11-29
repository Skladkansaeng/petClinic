from django.shortcuts import render
import json
from django.http import JsonResponse
from user.models import user
from createStaff.models import staff
import uuid
import base64
import hashlib
# # Create your views here.
# def staff(request):
#     return render(request, 'staff.html')
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def createUser(request):
    print('test')
    obj = json.loads(request.body.decode('utf-8'))
    print(obj)
    objUser = user.objects.all()
    for u in objUser:
        if u.username == obj['username']:
            return JsonResponse({"w": "cancel"})

    password_hash = hash_password(obj['password'])
    db = user(name = obj['firstname'] , surname = obj['lastname'] , tel =obj['tel'] ,
    email= obj['email'] , username= obj['username'], password= password_hash)
    db.save()
    return JsonResponse({"w": "wr"})

def get_userInfo(request):
    # print("fffffffffff")
    objUser = user.objects.all()
    obj = json.loads(request.body.decode('utf-8'))
#     print(obj)
    lst = []
    findUser = obj['str_input']
    for pn in objUser:
        if pn.name[:len(findUser)].lower() == findUser :
                d={"value": pn.name+ " "+ pn.surname,"link": pn.pk}
                lst.append(d)

    return JsonResponse(lst, safe=False)

def fonTest(req,pk):
    pk = pk.encode()
    decoded_data = base64.b64decode(pk)
    pk = decoded_data.decode()
    obj = staff.objects.get(pk=pk)
    context={"name": obj.name,"surname": obj.surname}
    # context={"name":'d',"surname":'p'}
    return render(req,'staff.html',context)
