from django.shortcuts import render
from user.models import user
# Create your views here.
def userpage(request):
    return render(request, 'user.html')

def fonTest(req,pk):
    obj = user.objects.get(pk=pk)
    context={"name": obj.name,"surname": obj.surname}
    # context={"name":'d',"surname":'p'}
    return render(req,'staff.html',context)