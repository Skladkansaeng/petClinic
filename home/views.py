from django.shortcuts import render
import json
from django.http import JsonResponse
from user.models import user
from createStaff.models import staff
import uuid
import hashlib
# Create your views here.
def home(request):
    return render(request, 'index.html')
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def checkUser(request):
    obj = json.loads(request.body.decode('utf-8'))
    # print(obj)
    
    # password_hash = obj['password']
    objUser = user.objects.filter(username=obj['username'])
    objStaff = staff.objects.filter(username=obj['username'])
    # print(objUser[0].password)
    print(len(objUser))
    # status = check_password(objUser[0].password,obj['password'])
    # if status :
    #     status = check_password(objStaff[0].password,obj['password'])

    
    if len(objUser) == 0 and len(objStaff) == 0 :
        return JsonResponse({"status": "No"})
    elif len(objStaff) == 1 :
        password_hash = objStaff[0].password
        if check_password(objStaff[0].password,obj['password']):
            st = staff.objects.get(username=obj['username'], password=password_hash)
            res = JsonResponse({"status": st.status,"pk": st.pk})
        # set_cookie(res,'YAY','slkdngsdfigskfngsdlfng')
            return res
    else:
        password_hash = objUser[0].password
        if check_password(objUser[0].password,obj['password']):
            us = user.objects.get(username=obj['username'], password=password_hash)
            res = JsonResponse({"status": "User", "pk": us.pk})
            # set_cookie(res,'YAY','tyuiopoiughjolplkjhjkl')
            return res