from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user

# Create your views here.



def home(request):
    return render(request, 'data/home.html')

@login_required(login_url='loginpage')
def reports(request):

    bireport = bireports.objects.all()

    context = {'bireport':bireport}

    return render(request,'data/reports.html', context)


@unauthenticated_user
def loginpage(request):
   
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/reports/')
            else:
                messages.info(request, 'Username or Password Incorrect')
            
    
    context = {}

    return render(request,'data/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('/')

@unauthenticated_user
def usercreation(request):

    createuser = CreateUserForm()
    if request.method == "POST":
            createuser = CreateUserForm(request.POST)
            if createuser.is_valid():
                createuser.save()

                user = createuser.cleaned_data.get('first_name')

                messages.success(request,'Account Created for ' + user)
                return redirect('/loginpage/')

    context = {'createuser':createuser}
    return render(request, 'data/usercreation.html', context)

def userPage(request):
    context = {}

    return render(request, 'data/user.html', context)


@login_required(login_url='loginpage')
def createaccount(request):

    form = StaffForm()

    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reportusers/')

    context = {'form':form}
    return render(request,'data/createaccount.html', context)


@login_required(login_url='loginpage')
def updateaccount(request, pk):
    
    staffuser = staffmembers.objects.get(id=pk)
    form = StaffForm(instance=staffuser)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staffuser)
        if form.is_valid():
            form.save()
            return redirect('/reportusers/')

    context ={'form':form}
    return render(request, 'data/updateaccount.html', context)


@login_required(login_url='loginpage')
def deleteaccount(request):

    context ={}
    return render(request, 'data/deleteaccount.html', context)


@login_required(login_url='loginpage')
def reportusers(request):

    reportusers = staffmembers.objects.all()



    context = {'reportusers':reportusers}
    return render(request, 'data/reportusers.html', context)


@login_required(login_url='loginpage')
def newreport(request):

    newreportform = NewReportForm()

    
    if request.method == 'POST':
        newreportform = NewReportForm(request.POST)
        if newreportform.is_valid():
            newreportform.save()
            return redirect('/reports/')
        
    context = {'newreportform':newreportform}
    return render(request, 'data/newreport.html', context)


@login_required(login_url='loginpage')
def updatereport(request, pk):

    reportkey = bireports.objects.get(id=pk)
    newreportform = NewReportForm(instance=reportkey)
    if request.method == 'POST':
        newreportform = NewReportForm(request.POST, instance=reportkey)
        if newreportform.is_valid():
            newreportform.save()
            return redirect('/reports/')

    context ={'reportkey':reportkey,'newreportform':newreportform}
    return render(request, 'data/updatereport.html', context)




def deletereport(request,pk):

    reportkey = bireports.objects.get(id=pk)

    if request.method == 'POST':
        reportkey.delete()
        return redirect('/reports/')

    context = {'item':reportkey}
    return render(request, 'data/deletereport.html', context)


@login_required(login_url='loginpage')
def userprofile(request, pk):

    staffuser = staffmembers.objects.get(id=pk)

    context = {'staffuser':staffuser}
    return render(request, 'data/userprofile.html', context)
