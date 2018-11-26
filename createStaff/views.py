from django.shortcuts import render
from createStaff.models import staff
import json
from django.http import JsonResponse
from home.views import home
# Create your views here.
def create(request):
    return render(request, 'newStaff.html')
    
def pushdb(request):
    print("test")
    obj = json.loads(request.body.decode('utf-8'))
    print(obj)
    db = staff(name = obj['firstname'] , surname = obj['lastname'] , tel =obj['tel'] , email= obj['email'] , status = obj['status'] , username = obj['username'] , password = obj['password'])
    db.save()
    # print('Name:',obj['name'])
    # print('Password:',obj['pass'])
    # return render(request, 'index.html')
    return JsonResponse({"x": "doctor"})
