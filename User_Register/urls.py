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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from User_Register import settings
from User_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('next', views.next_view, name='next'),
    path('logout',views.logout_view, name='logout'),
    path('button-click', views.button_click_view, name='button_click'),
    path('profile-page-click', views.profile_page_click, name='profile_page_click'),
    path('create', views.create_profile, name='create_profile'),
    # path('profiles', views.profile_list, name='profile_list'),
    path('update_profile',views.update_profile_view,name='update_profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
