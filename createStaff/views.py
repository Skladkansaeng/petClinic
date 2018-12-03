from django.shortcuts import render,redirect
from createStaff.models import staff
from user.models import user
import json
from django.http import JsonResponse
from home.views import home
import uuid
import hashlib
import base64

# Create your views here.
def create(req):
    insession = req.session.get('username')
    objStaff = staff.objects.filter(username = insession)     
    objUser = user.objects.filter(username = insession)
    if(len(objStaff) > 0 ):
        if objStaff[0].status == 'Staff':
                return render(req, 'newStaff.html')
        else:
                pk_str = str(objStaff[0].pk).encode()
                encoded_data = base64.b64encode(pk_str)
                encoded_data = str(encoded_data)[2:-1]
                str_url = '../doctor/'+encoded_data
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

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def pushdb(req):    
    insession = req.session.get('username')
    objStaff = staff.objects.filter(username = insession)     
    if(len(objStaff) > 0 ):
        obj = json.loads(req.body.decode('utf-8'))
        print(obj)
        password_hasg = hash_password(obj['password'])
        objStaff = staff.objects.all()
        for u in objStaff:
                if u.username == obj['username']:
                        return JsonResponse({"w": "cancel"})
        print(password_hasg)
        db = staff(name = obj['firstname'] , surname = obj['lastname'] , tel =obj['tel'] , email= obj['email'] , status = obj['status'] , username = obj['username'] , password = password_hasg)
        db.save()
        return JsonResponse({"x": "doctor"})
    else:
                print ("in")
                req.session['username'] = ''
                return JsonResponse({"w": "refresh"})

