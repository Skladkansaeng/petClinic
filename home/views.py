from django.shortcuts import render
import json
from django.http import JsonResponse
from user.models import user
from createStaff.models import staff
# Create your views here.
def home(request):
    return render(request, 'index.html')

def checkUser(request):
    obj = json.loads(request.body.decode('utf-8'))
    print(obj)
    objUser = user.objects.filter(username=obj['username'],password=obj['password'])
    objStaff = staff.objects.filter(username=obj['username'],password=obj['password']).values('status')
    print(objUser)
    print(str(objStaff))
    if not objUser and not objStaff:
        return JsonResponse({"status": "No"})
    if not objUser:
        return JsonResponse({"status": str(objStaff)})
    return JsonResponse({"status": "User"})
