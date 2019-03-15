from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

# def signup(request):
#     if request.method == 'POST':
#         form = forms.SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = forms.SignUpForm()
#     return render(request, 'signup.html', {'form': form})


# def signup_view(request):
#     if request.method == 'POST':
#         print("234567")
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # user = form.cleaned_data['get_user']
#             # auth_login(request, user)
#             return redirect('videoapp:home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

def prof_signup_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            new_user = User.objects.create_user(username=username, email=email, password=password, is_staff=True)
            # new_user = form.save(commit=False)
            new_user.save()
            auth_login(request, new_user)
            return redirect('videoapp:home')
    else:
        form = forms.SignUpForm()
    return render(request, 'Prof_Sign_up.html', {'form': form})

def stud_signup_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            new_user = User.objects.create_user(username=username, email=email, password=password)
            # new_user = form.save(commit=False)
            new_user.save()
            auth_login(request, new_user)
            return redirect('videoapp:home')
    else:
        form = forms.SignUpForm()
    return render(request, 'Stud_Sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('videoapp:home')

    else:
        form =  AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logout_view(request):
    #if request.method == 'POST':
    auth_logout(request)
    return redirect('videoapp:home')



















# def index(request):
#     return render(request,'authentication/index.html')
#
#
# def special(request):
#     return HttpResponse("You are logged in !")
#
#
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))
#
#
# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileInfoForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             if 'profile_pic' in request.FILES:
#                 print('found it')
#                 profile.profile_pic = request.FILES['profile_pic']
#             profile.save()
#             registered = True
#         else:
#             print(user_form.errors,profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileInfoForm()
#     return render(request,'dappx/registration.html',
#                           {'user_form':user_form,
#                            'profile_form':profile_form,
#                            'registered':registered})
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Your account was inactive.")
#         else:
#             print("Someone tried to login and failed.")
#             print("They used username: {} and password: {}".format(username,password))
#             return HttpResponse("Invalid login details given")
#     else:
#         return render(request, 'authentication/login.html', {})
