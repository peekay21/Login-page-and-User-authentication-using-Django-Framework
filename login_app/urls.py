from django.contrib import admin
from django.urls import path, include
from login_app import views
urlpatterns = [
    path('',views.loginpage, name='loginpage'),
    path('loginauth/',views.loginauth, name='loginauth'),
    path('logout/', views.logout, name='logout'),
]
