from cProfile import Profile

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
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
        return render(request, 'index.html')
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
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
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
        context = {'form': form}
    return render(request, 'create profile.html', {'form': form})


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


# def upload_video(request):
#     if request.method == 'POST':
#         form = VideoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#         else:
#             form = VideoForm()
#         return render(request, 'create_profile.html', {'form': form})


class SignUpView(FormView):
    template_name = "home.html"
    form_class = SignUpForm
    success_url = "login"


class LoginView(FormView):
    template_name = "index.html"
    form_class = SignUpForm
    success_url = "next"


class ProfilePageView(FormView):
    template_name = "create profile.html"
    form_class = ProfileForm
    success_url = "next"


class UpdateProfileView(FormView):
    template_name = 'update_profile.html'
    form_class = UpdateProfileForm
    success_url = 'profile'


# class UploadVideoView(FormView):
#     template_name = 'create_profile.html'
#     form_class = VideoForm
#     success_url = 'profile'


class MultiFunctionView(View):

    def get(self, request, *args, **kwargs):
        action = kwargs.get('action')

        if action == 'signup':
            form = SignUpForm()
            return render(request, 'home.html', {'form': form})

        elif action == 'login':
            return render(request, 'index.html')

        elif action == 'next':
            return render(request, 'next.html')

        elif action == 'logout':
            logout(request)
            return redirect('signup')

        elif action == 'create_profile':
            userprofile = None
            try:
                userprofile = request.user.userprofile
            except UserProfile.DoesNotExist:
                userprofile = UserProfile(user=request.user)
                userprofile.save()

            form = ProfileForm(instance=userprofile)
            return render(request, 'create_profile.html', {'form': form})

        elif action == 'update_profile':
            profile_form = UpdateProfileForm(instance=request.user.userprofile)
            return render(request, 'update_profile.html', {'profile_form': profile_form})

        elif action == 'button_click':
            return redirect('login')

    def post(self, request, *args, **kwargs):
        action = kwargs.get('action')

        if action == 'signup':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            return render(request, 'home.html', {'form': form})

        elif action == 'login':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('next')
            return render(request, 'index.html')

        elif action == 'create_profile':
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            form = ProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('next')
            return render(request, 'create_profile.html', {'form': form})

        elif action == 'update_profile':
            profile_form = UpdateProfileForm(request.POST, instance=request.user.userprofile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile')
            return render(request, 'update_profile.html', {'profile_form': profile_form})
