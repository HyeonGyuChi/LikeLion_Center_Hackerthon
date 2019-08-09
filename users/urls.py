"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from allauth.account.views import SignupView, LoginView, LogoutView
from . import views
from users import urls

app_name = 'users'
urlpatterns = [
    path('signup', SignupView.as_view(), name="account_signup"),    # account_signup
    path('login', LoginView.as_view(), name="account_login"),       #  account_login
    path('logout', LogoutView.as_view(), name="account_logout"),    # account_logout
    path('mypage', views.mypage, name="mypage"),
    path('coin_add/<int:amount>', views.coin_add, name="coin_add"),
    path('coin_sub/<int:amount>', views.coin_sub, name="coin_sub"),
]