from django.shortcuts import render,redirect
from .forms import Register
from django.contrib.auth import authenticate,login,logout
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
			return redirect('login')
	else:
		form = Register()
	return render(request,'hospital/register.html',{'form':form})


def Login(request):
	error = ""
	if request.method=='POST':
		u = request.POST['uname']
		p = request.POST['pwd']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error = "yes"
			else:
				error = "no"
		except:
			error = "no"
	d = {'error':error}
	return render(request,'hospital/login.html',d)