from django.shortcuts import render,redirect
from .forms import Register
from .models import*
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


def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        s = request.POST['specialization']
        
        try:
            Doctor.objects.create(name=n,contact=c,specialization=s)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'hospital/add_doctor.html',d)



def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
        
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'hospital/view_doctor.html',d)


def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
        
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        a = request.POST['age']
        g = request.POST['gender']
        ad = request.POST['address']
        
        try:
            Patient.objects.create(name=n,contact=c,age=a,gender=g,address=ad)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'hospital/add_patient.html',d)

    
def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
        
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'hospital/view_patient.html',d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
        
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')