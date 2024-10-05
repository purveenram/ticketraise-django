from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest
from django.views.generic import ListView
import datetime
import json
from .models import *
from .forms import *

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('login')

def home(request):
    userId = request.session.get("userId")
    try:
        querys = QueryDetails.objects.filter(studentIdInQuery=userId)
    except:
        querys = None
    return render(request, 'home.html',{'querys':querys})

def credentialCheck(request):
    if request.method == 'POST':
        buttonClick = request.POST.get('buttonClick')
        if buttonClick == 'loginButton':
            email = request.POST.get('userEmail')
            password = request.POST.get('userPass')
            user = authenticate(request, studentEmail=email, studentPassword=password)
            if user is not None:
                request.session["userId"] = user.id
                return redirect('home')
        elif buttonClick == 'signupButton':
            return redirect("studentSignup")
    return redirect('login')

def newTicket(request):
    userId = request.session.get("userId")
    if userId:
         user = StudentDetails.objects.get(id=userId)
    studentRegNo = user.studentRegNo
    return render(request, 'newTicket.html',{"studentRegNo":studentRegNo})

def addQuery(request):
    form = QueryDetailsForm()
    if request.method == 'POST':
        form = QueryDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return redirect('newTicket')

def removeInQuery(request, queryId):
    item = get_object_or_404(QueryDetails, id=queryId)
    item.delete()
    return redirect('home')

def studentSignup(request):
    return render(request, 'studentSignup.html')

def addStudent(request):
    form = StudentDetailsForm()
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['studentEmail']
            regNo = form.cleaned_data['studentRegNo']
            if StudentDetails.objects.filter(studentEmail=email):
                return render(request, 'login.html', {'error_message': 'This Email Id Already Exist !'})
            if StudentDetails.objects.filter(studentRegNo=regNo):
                return render(request, 'login.html', {'error_message': 'This Register No Already Exist !'})
            else:
                form.save()
                return redirect('login')
    return redirect('studentSignup')