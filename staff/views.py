from django.shortcuts import render
import json
from django.http import JsonResponse
from user.models import user
# Create your views here.
def staff(request):
    return render(request, 'staff.html')
def createUser(request):
    print('test')
    obj = json.loads(request.body.decode('utf-8'))
    print(obj)
    db = user(name = obj['firstname'] , surname = obj['lastname'] , tel =obj['tel'] ,
    email= obj['email'] , username= obj['username'], password= obj['password'] )
    db.save()
    return JsonResponse({"w": "wr"})
