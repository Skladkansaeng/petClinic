"""petClinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from createStaff import views as createStaffViews
from staff import views as staffViews
from home import views as homeViews
from doctor import views as views_doctor
from user import views as userViews
from userInfo import views as info_doctor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createStaff/', createStaffViews.create),
    path('', homeViews.home),
    path('createStaff/created/', createStaffViews.pushdb),
    path('doctor/',views_doctor.doctor),
    path('doctor/createMedical',views_doctor.createMedical),
    path('doctor/createVaccine',views_doctor.createVaccine),
    path('doctor/doctorData/',views_doctor.sendJson),
    path('doctor/Makeappointment/',views_doctor.Makeappointment),
    path('doctor/getMedical/',views_doctor.getMedical),
    path('doctor/getVaccine/',views_doctor.getVaccine),
    path('staff/', staffViews.staff),
    path('user/',userViews.userpage),
    path('oak/', staffViews.createUser),
    path('staff/getuserInfor/', staffViews.get_userInfo),
    path('check/', homeViews.checkUser),
    path('getJason/',info_doctor.getDataJson),
    path('userInfo/newPet/',info_doctor.newPet),
    path('makeQueue/',info_doctor.makeQueue),
    path('userInfo/<int:pk>',info_doctor.userInfo),
    path('user/<int:pk>',userViews.fonTest),
    path('doctor/<int:pk>', views_doctor.fonTest),
    path('staff/<int:pk>', staffViews.fonTest),
    path('user/editProfile/<int:pk>',userViews.editProfile),
    path('user/userData/<int:pk>',userViews.userData),
    path('user/appData/<int:pk>',userViews.appData),

]
