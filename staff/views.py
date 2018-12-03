from django.shortcuts import render,redirect
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
    objUser = user.objects.all()
    obj = json.loads(request.body.decode('utf-8'))
    lst = []
    findUser = obj['str_input']
    for pn in objUser:
        if pn.name[:len(findUser)].lower() == findUser :
                d={"value": pn.name+ " "+ pn.surname,"link": pn.pk}
                lst.append(d)

    return JsonResponse(lst, safe=False)

def fonTest(req,pk):  
    insession = req.session.get('username')
    objStaff = staff.objects.filter(username = insession)     
    objUser = user.objects.filter(username = insession)    
    if(len(objStaff) > 0 ):
        pk = pk.encode()
        decoded_data = base64.b64decode(pk)        
        pk = decoded_data.decode()
        if int(pk) == objStaff[0].pk:        
            obj = staff.objects.get(pk=objStaff[0].pk)
            context={"name": obj.name,"surname": obj.surname}    
            return render(req,'staff.html',context)
        else:
            pk_str = str(objStaff[0].pk).encode()
            encoded_data = base64.b64encode(pk_str)
            encoded_data = str(encoded_data)[2:-1]
            if objStaff[0].status == 'Doctor':
                str_url = '../doctor/'+encoded_data
            else :
                str_url = '../staff/'+encoded_data
            return redirect(str_url)
    elif(len(objUser) > 0 ):
            pk_str = str(objUser[0].pk).encode()
            encoded_data = base64.b64encode(pk_str)
            encoded_data = str(encoded_data)[2:-1]
            str_url = '../user/'+encoded_data
            return redirect(str_url)   
    else:
        req.session['username'] = ''
        return render(req,'index.html')