from imp import source_from_cache
from tokenize import Name
from urllib import request

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import appointment,contact
#Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def service(request):
    return render(request,"service.html")
def history(request):
    return render(request,"history.html")
def appointment1(request):
    if request.method == 'POST':
        hospitalname = request.POST['hospitalname']
        specialistname = request.POST['specialistname']
        pname = request.POST['pname']
        email = request.POST['m1']
        date = request.POST['hdate']
        time = request.POST['t1']
        age = request.POST['a1']
        print(hospitalname, specialistname, pname)
        user3 = appointment(hospitalname=hospitalname, specialistname=specialistname, pname=pname, mail=email, date=date, time=time, age=age)
        user3.save()
        print('appointment booked')
        return redirect('/appointment')
    return render(request, "appointment.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = auth.authenticate(username=username, password=password)
        print(username, password)
        if user1 is not None:
            auth.login(request, user1)
            messages.success(request, "successfully logged in")
            return redirect('/home')
        else:
            messages.success(request, "Authentication failed")
            return redirect("/login")
    return render(request, 'login.html')
def registration(request):
    if request.method == 'POST':
        username = request.POST['uname']
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        passwd = request.POST['password']
        # messages.info(request, 'username already exists')
        date = datetime.date.today()
        user3 = User.objects.create_user( username = username , first_name = fname, last_name = lname, password = passwd, email = email, date_joined = date)
        user3.save()
        print('user created')
        return redirect('/login')
    return render(request, "registration.html")

def history(request):
    hist = appointment.objects.all()
    print(hist)
    return render(request, 'history.html', {'History': hist})

def loginout(request):
    logout(request)
    return redirect('/login')

def fp1(request):
    c = None
    return render(request, 'fp.html')


@csrf_exempt
def fp(request):
    mail = request.POST['email']
    send_mail('Changing Password',  # subject
              'http://127.0.0.1:8000/cp/',
              'iamvinayy100@gmail.com',  # from
              [mail],  # to
              fail_silently=False,
              )

    return render(request, 'sp.html')




@csrf_exempt
def cp(request):
    return render(request, 'cp.html')


@csrf_exempt
def cp1(request):
    username = request.POST['username']
    password = request.POST['Password']
    password1 = request.POST['re-enter Password']
    if password == password1:
        u = User.objects.get(username=username)
        u.set_password(password1)
        u.save()
        return redirect('/login')
    else:
        return redirect('/cp')




    # def contactform(request):
    #     if request.method == 'POST':
    #         name = request.POST['name']
    #         email = request.POST['mail']
    #         message = request.POST['msg']
    #         subject = request.POST['sub']
    #         if request.user.is_authenticated:
    #             username = request.user.username
    #         print(name, email, subject, message)
    #         contactform = contact(name=name, mail=email, sub=subject, msg=message)
    #         contactform.save()
    #         msg = "Your Problem has been initiated to administrator! We will contact you with in 24 hours"
    #         send_mail('Query',  # subject
    #                   msg,
    #                   'iamvinayy100@gmail.com',  # from
    #                   [request.user.email],  # to
    #                   fail_silently=False,
    #                   )
    #
    #         messages.success(request, "Message sent.")
    #
    #     return render(request, 'contact.html')
