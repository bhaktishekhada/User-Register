from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from User_app.models import UserProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birthdate', 'gender', 'city', 'profile_picture')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"


