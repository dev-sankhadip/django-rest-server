from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import jwt
from .models import UserModel


def index(request):
    return render(request,'shop/index.html')

def signup(request):
    return render(request,'shop/signup.html')

def login(request):
    return render(request,'shop/login.html')

def handleSignup(request):
    if request.method=='POST':
        
        # get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']

        print(password)
        # check for error input
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('/shop/login')

    else:
        return HttpResponse("404 - not found")

def handleLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully loggedin")
            return redirect('/shop/signup')
        else:
            messages.error(request,"not valid")
            return redirect('/shop/login')

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully loggedout")



def customRegister(request):
    if request.method=='POST':
        print(request.body)
    return HttpResponse("ok");


def customLogin(request):
    print(request.body)
    return HttpResponse("ok")