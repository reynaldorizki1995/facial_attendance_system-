from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from matplotlib.style import context
# Create your views here.

from .models import *
from .forms import CreateUserForm


# def index(request):
#     if not request.user.is_authenticated:
#         return redirect(login)
#     return render(request,"index.html")

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             _login(request, user)
#             return redirect(index)
#         else:
#             messages.info(request, 'Username OR password is incorrect')
#     elif request.method == 'GET':
#         if request.user.is_authenticated:
#             return redirect(index)
#         return render(request,'login.html')

# def register(request):
#     if not request.user.is_authenticated:
#         return redirect(login)
#     else:
#         form = CreateUserForm()
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('id')
#                 messages.success(request, 'Account was created for ' + user)

#                 return redirect('login')
#         context = {'form':form}
#         return render(request,"register.html", context)

def index(request):
    if not request.user.is_authenticated:
        return redirect(login)
    return render(request,"index.html")

def register(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)




