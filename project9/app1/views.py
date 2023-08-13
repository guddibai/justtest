from django.shortcuts import render, redirect
from app1.models import StudentModel, LoginModel
from django.contrib import messages


def main1(request):
    return render(request, "home.html")


def studentlogin(request):
    return render(request, "studentlogin.html")


def studentregistration(request):
    return render(request, "studregister.html")


def savestuddata(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    contact = request.POST.get("t3")
    gender = request.POST.get("t4")
    username = request.POST.get("t5")
    password = request.POST.get("t6")
    type = 'student'
    stm = StudentModel(name=name, age=age, contactno=contact, gender=gender, username=username)
    stm.save()
    lm = LoginModel(username=username, password=password, type=type)
    lm.save()
    messages.success(request, "Thanks For Registration")
    return redirect('register')


def forgotpassword(request):
    return render(request, "forgotpassword.html")


def changepass(request):
    username = request.POST.get("f1")
    contact = request.POST.get("f2")
    password = request.POST.get("f3")
    conf_pass = request.POST.get("f4")

    try:
        StudentModel.objects.get(username=username, contactno=contact)
        if password == conf_pass:
            LoginModel.objects.filter(username=username).update(password=password)
            return render(request, "forgotpassword.html", {"msg": "password updated successfully"})
        else:
            return render(request, "forgotpassword.html", {"msg": "plz enter same password"})
    except StudentModel.DoesNotExist:
        messages.error(request, "Invalid Details")
        return render(request, "forgotpassword.html")


def adminlogin(request):
    return render(request, "adminlogin.html")


def adminhome(request):
    username = request.POST.get("a1")
    password = request.POST.get("a2")
    type = 'admin'
    try:
        LoginModel.objects.get(username=username, password=password, type=type)
        return render(request, "adminhome.html")
    except LoginModel.DoesNotExist:
        return render(request, "adminlogin.html", {"msg": "You are not Authorised to access this account"})


def viewallstud(request):
     allstd = StudentModel.objects.all()
     return render(request, "viewallstud.html",{"data":allstd})


def deletestud(request):
    return render(request, "deletestud.html")


def stdlogin_check(request):
    un = request.POST.get("s1")
    pa = request.POST.get("s2")
    yt = 'student'
    try:
        LoginModel.objects.get(username=un, password=pa, type=yt)
        return render(request, "studenthome.html", {"name": un})  # sending username if username password is correct
    except LoginModel.DoesNotExist:
        messages.error(request, "Invalid Credentials")
        return render(request, 'studentlogin.html')


def studenthome(request):
    uname = request.GET.get("un")
    return render(request, "studenthome.html", {"name": uname})


def viewprofile(request):
    uname = request.GET.get("un")
    stu = StudentModel.objects.get(username=uname)
    return render(request, "viewprofile.html", {"name": uname, "data": stu})


def updateprofile(request):
    uname = request.GET.get("un")
    stu = StudentModel.objects.get(username=uname)
    return render(request, "updateprofile.html", {"name": uname, "data": stu})


def updatedata(request):
    na = request.POST.get("u1")
    ag = request.POST.get("u2")
    co = request.POST.get("u3")
    ge = request.POST.get("u4")

    un = request.POST.get("u5")

    StudentModel.objects.filter(username=un).update(name=na, age=ag, contactno=co, gender=ge)

    return render(request, "studenthome.html", {"name": un})


def deletestd(request):
    uname = request.GET.get("un")
    StudentModel.objects.get(username=uname).delete()
    allstd = StudentModel.objects.all()
    return render(request, "viewallstud.html",{"data":allstd})