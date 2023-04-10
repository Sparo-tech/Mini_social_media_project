from django.contrib import auth
from django.contrib.auth.views import PasswordChangeView
from django.urls import path,include
from .views import RegisterView,ChangePassword,PasswordChanged,userlogin,userlogout


app_name='users'

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',userlogin,name='login'),
    # path('login/',UserLogin.as_view(),name='login'),
    path('change-password/',ChangePassword.as_view(),name='password-reset'),
    path('password-change-done/',PasswordChanged.as_view(),name='password_change_done'),
    path('logout', userlogout, name='logout')
   
]
