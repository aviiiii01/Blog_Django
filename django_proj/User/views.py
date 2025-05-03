from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if username and password and email:
            if(User.objects.filter(email=email).exists()):
                messages.error(request,f"Sorry Mr./Mrs {username} You are already registered from this {email}..!")
                return redirect('homepage')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request,f"Successfully registered Mr./Mrs {username}")
            return redirect('homepage')
        else:
            messages.error(request,f"Check your credentials")
            return redirect('register')
    return redirect('homepage')

        
        

# def loginn(request):
#     if(request.method=="POST"):
#         username=request.POST.get("username")
#         password=request.POST.get("password")
#         if(username and password):
#             user=authenticate(request, username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,f"Welcome Mr./Mrs {username}")
#                 return redirect('homepage')
#         messages.success(request,f"Welcome Mr./Mrs {username}")
#         return redirect('homepage')
#     return render(request,'blog/home.html')
@login_required
def logoutt(request):
    logout(request)
    return redirect("homepage")

@login_required
def loginview(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
          # if you're using it

        if not username or not password:
            messages.error(request, "Please enter both username and password")
            return render(request, "blog/home.html")

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, f'{username} Baby Welcome!!!')
            return redirect("homepage")
        else:
            messages.error(request, "Baby check the credentials")
            return redirect("homepage")

    return render(request, "blog/home.html")