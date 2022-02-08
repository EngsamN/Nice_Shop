from django.shortcuts import  render, redirect
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def singupregster(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginView_form.html')
    context = {'form': form}
    return render(request, 'singup.html', context)

class AdminLogin(LoginView):
    form = LoginForm
    template_name = 'LoginView_form.html'
    # def getuser_name():
    #     adminuser=User.objects.all()
    #     return adminuser
       
                

    def get(self, request, **args):
        # if request.user.is_authenticated:
        #     return redirect('index', permanent=False)
      
        context = {  'form': LoginForm()}
    
        return render(request, self.template_name,context)




@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login', permanent=False)

def register_page(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    context = {'form': form}

    return render(request, 'users/register.html', context)


 
        