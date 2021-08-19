from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('add_doctor/',views.Add_Doctor, name='add_doctor' ),
    path('view_doctor/',views.View_Doctor, name='view_doctor' ),
    path('delete_doctor/<int:pid>/',views.Delete_Doctor, name='delete_doctor' ),



    path('login/', auth_views.LoginView.as_view(template_name='hospital/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='hospital/logout.html'), name='logout'),


    
    
]

