from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
  
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# from.forms import AuthenticationForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html" 
    success_url = reverse_lazy('users:login') 


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,'logged in succesfuly')
            
            if user.profile.count_following() < 1 :
                return redirect('profiles:all-profiles')
            else:
                return redirect('posts:home')
        else:
            messages.info('incorrect credentials')    
    return render(request,'registration/login.html', )        
            


class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name =  "registration/password_change_form.html" 


class PasswordChanged(PasswordChangeDoneView):
    template_name =  "registration/password_change_done.html" 
    
    
def userlogout(request):
    logout(request)
    return redirect('users:login')    
    
