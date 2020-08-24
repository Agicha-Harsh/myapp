from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django import forms


# Create your views here.
#from forms import CreateUserForm

def indexView(request):
	return render(request,'index.html')

@login_required
def dashboardView(request):
	return render(request,'dashboard.html')

def registerView(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')
	else:
		form = CreateUserForm()
	return render(request,'registration/register.html',{'form':form})

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']