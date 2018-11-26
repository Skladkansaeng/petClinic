from django.contrib import admin

# Register your models here.
from user.models import user,mypet
# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ['name','surname','tel','email','username','password']
class mypetAdmin(admin.ModelAdmin):
    list_display = ['user','name','type','birthDate','age','breed','sickness']

admin.site.register(user,userAdmin)
admin.site.register(mypet,mypetAdmin)
