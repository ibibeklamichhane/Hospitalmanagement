from django.shortcuts import render

def home(request):
     return render(request, 'hospital/home.html', {})

def about(request):
     return render(request, 'hospital/about.html', {})

def contact(request):
     return render(request, 'hospital/contact.html', {})