from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import DoctorForm, PatientForm, DoctorLogin, PatientLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.
def home(request):
    return render(request,'home.html')

def drsign(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(drlogin)
    else:
        form = DoctorForm()
    return render(request,'drsign.html',{'form':form})

def ptsign(request):
    if request.method == 'POST':
        form = PatientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(ptlogin)
    else:
        form = PatientForm()
    return render(request,'ptsign.html',{'form':form})
@login_required(login_url=home)
def drlogin(request):
    if request.method == 'POST':
        form = DoctorLogin(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(profile)
    else:
        form = DoctorLogin()
    return render(request,'drlogin.html',{'form':form})


def ptlogin(request):
    if request.method == 'POST':
        form = PatientLogin(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(profile)
    else:
        form = PatientLogin()
    return render(request,'ptlogin.html',{'form':form})
@login_required(login_url=home)
def profile(request):
    return render(request,'profile.html')


def logout_view(request):
    logout(request)
    return redirect(home)