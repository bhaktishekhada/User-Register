"""
URL configuration for User_Register project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from User_app import views
from django.urls import path

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path("cbv/", views.SignUpView.as_view(), name="cbv_signup_view"),
    path('login', views.login_view, name='login'),
    path('cbv/', views.LoginView.as_view(), name="cbv_login_view"),
    path('next', views.next_view, name='next'),
    path('logout', views.logout_view, name='logout'),
    path('button-click', views.button_click_view, name='button_click'),
    path('profile-page-click', views.profile_page_click, name='profile_page_click'),
    path('cbv/' ,views.ProfilePageView.as_view(), name="cbv_profile_page_view" ),
    path('create', views.create_profile, name='create_profile'),
    path('update_profile', views.update_profile_view, name='update_profile'),
    path('cbv/', views.UpdateProfileView.as_view(), name="cbv_update_profile_view"),
    # path('upload/', views.upload_video, name='upload_video'),
]