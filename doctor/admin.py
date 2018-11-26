from django.contrib import admin
from doctor.models import queue
from doctor.models import medical
from doctor.models import vaccine , appointment
# Register your models here.
class queueAdmin(admin.ModelAdmin):
    list_display = ['pet_name','pet_type','pet_weight','pet_HeartRate','pet_RestRate','pet_Dehydration','pet_want']
class medicalAdmin(admin.ModelAdmin):
    list_display = ['pet_name']
class vaccineAdmin(admin.ModelAdmin):
    list_display = ['pet_name']
class appointmentAdmin(admin.ModelAdmin):
    list_display = ['pet_name']


admin.site.register(queue,medicalAdmin)
admin.site.register(medical,medicalAdmin)
admin.site.register(vaccine,vaccineAdmin)
admin.site.register(appointment,appointmentAdmin)