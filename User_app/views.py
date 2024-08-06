from cProfile import Profile

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .forms import SignUpForm, ProfileForm, UpdateProfileForm
from django.views.decorators.cache import never_cache
# from .models import Profile
# from .forms import ProfileForm

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import UserProfile


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'home.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # username = request.POST
            login(request, user)
            return redirect('next')
    else:
        return render(request, 'index.html')


@never_cache
@login_required(login_url='login')
def next_view(request):
    return render(request, 'next.html')


@never_cache
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('signup')


def button_click_view(request):
    return redirect('login')


def profile_page_click(request):
    if request.method == 'POST':
        user_profile,created=UserProfile.objects.get_or_create(user=request.user)
        form = ProfileForm(request.POST,request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('next')
    else:
        userprofile = None
        try:
            userprofile = request.user.userprofile
        except Exception as e:
            print(e)
        form = ProfileForm(instance=userprofile)
        context={'form': form}
    return render(request, 'create profile.html',{'form': form})


def create_profile(request):
    return render(request, 'create_profile.html')


# def profile_list(request):
#     profiles = Profile.objects.get()
#     return render(request, 'profile_list.html', {'profiles': profiles})


@login_required
def update_profile_view(request):
    if request.method == "POST":
        profile_form = UpdateProfileForm(request.POST, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
        else:
            profile_form = UpdateProfileForm(instance=request.user.userprofile)
        return render(request, 'update_profile.html', {'profile_form': profile_form})
