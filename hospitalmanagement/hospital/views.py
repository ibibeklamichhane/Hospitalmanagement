from django.shortcuts import render,redirect
from .forms import Register

def home(request):
     return render(request, 'hospital/home.html', {})

def about(request):
     return render(request, 'hospital/about.html', {})

def contact(request):
     return render(request, 'hospital/contact.html', {})



def register(request):
	if request.method=="POST":
		form = Register(request.POST)
		if form.is_valid():
			print("HELLO")
			print(form)
			form.save()
			return redirect('home')
	else:
		form = Register()
	return render(request,'hospital/register.html',{'form':form})