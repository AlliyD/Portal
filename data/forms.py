from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class StaffForm(ModelForm):
    class Meta:
        model = staffmembers
        fields = '__all__'
 


class NewReportForm(ModelForm):
    class Meta:
        model = bireports
        fields = '__all__'
        widgets={
            'report_name' : forms.TextInput(attrs={'width':'100px'})
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']