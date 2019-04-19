from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from .forms import RegisterUser

# Create your views here.


def index(request):
    form = AuthenticationForm()
    return render(request, 'accounts/login.html',{"form":form})

def login(request):
     if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return render(request, 'base/home.html')
     else:
         form = AuthenticationForm()
     return render(request, 'accounts/login.html',{"form":form})

def all_users(request):
    users_list = User.objects.all()

    context ={"objects": users_list}
    return render(request, 'accounts/users_list.html',context)


def user_details(request,username): 

    user = User.objects.get(username= username)       

    print(user.first_name)
    context = {"user":user}    
    return render(request,'accounts/user_detail.html',context)



def edit(request,username):
    print(username)
    return

def register(request):     

    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'accounts/login.html')

    else:
        form = RegisterUser()   

    context = {"form":form}
    return render(request, 'accounts/register.html',context)
