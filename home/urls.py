from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [ 
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('signin/', views.signin, name="signin"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('image/', views.image, name="image")
]
