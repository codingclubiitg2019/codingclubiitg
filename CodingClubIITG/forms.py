from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from datetime import datetime

class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields= ['username','email','password']

class ProjectsForm(forms.ModelForm):
	
	date = forms.DateField(initial=datetime.today().strftime('%Y-%m-%d'), label='Date of Project',widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

	class Meta:
		model = Projects
		fields=['name','status','outline','details','prereq','date']
