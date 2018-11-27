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
    objStaff = staff.objects.filter(username=obj['username'],password=obj['password'])
    if not objUser and not objStaff:
        return JsonResponse({"status": "No"})
    elif not objUser:
        st = staff.objects.get(username=obj['username'], password=obj['password'])
        res = JsonResponse({"status": st.status,"pk": st.pk})
        # set_cookie(res,'YAY','slkdngsdfigskfngsdlfng')
        return res
    else:
        us = user.objects.get(username=obj['username'], password=obj['password'])
        res = JsonResponse({"status": "User", "pk": us.pk})
        # set_cookie(res,'YAY','tyuiopoiughjolplkjhjkl')
        return res