from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def loginpage(request):
     return render(request, 'login_page.html')

def loginauth(request):
     if request.method =='POST':
          login_username = request.POST['username']
          login_password = request.POST['password']

          user = authenticate(username =login_username, password = login_password)
          if user is not None:
               login(request, user)
               context ={
                    'login_user' : login_username,
                    
               }
               return render(request, 'loggedin_page.html',context)
          
          else:
               return render(request, 'login_page.html')



     return render(request, 'login_page.html')

def handlelogout(request):
     logout(request)
     return render(request, 'login_page.html')