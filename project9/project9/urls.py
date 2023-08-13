"""project9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main1),
    path('openhome/', views.main1, name="openhome"),
    path('studentlogin/', views.studentlogin, name="studentlogin"),
    path('register/', views.studentregistration, name="register"),
    path('savestuddata/', views.savestuddata, name="savestuddata"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('changepassword/', views.changepass, name="changepassword"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('viewallstud/', views.viewallstud, name="viewallstud"),
    path('deletestud/', views.deletestud, name="deletestud"),
    path('stdlogin_check/', views.stdlogin_check, name="stdlogin_check"),
    path('studenthome/', views.studenthome, name="studenthome"),
    path('viewprofile/', views.viewprofile, name="viewprofile"),
    path('updateprofile/', views.updateprofile, name="updateprofile"),
    path('updatedata/', views.updatedata, name="updatedata"),
    path('deletestd/', views.deletestd, name="deletestd")

]
