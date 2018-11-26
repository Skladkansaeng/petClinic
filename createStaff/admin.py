from django.contrib import admin
from createStaff.models import staff
# Register your models here.

class staffAdmin(admin.ModelAdmin):
    list_display = ['name','surname','tel','email','status','username','password']
admin.site.register(staff,staffAdmin)
