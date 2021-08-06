from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from.forms import EditUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login,logout

# Create your views here.
#P2C-21-027
def accounts(request):
    return render(request, 'accounts.html')

def home(request):
    return render(request, 'accounts.html')    


def signup(request):
    return render(request, 'signup.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')


#p2c-21-105
def profile(request):  
    if request.user.is_authenticated:
        fm=EditUser(instance=request.user)
        return render(request,'profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def register(request):                         
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1!=pass2:
            messages.warning(request,'Password not matched')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'username already exist')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already exist')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=fname, last_name=lname, username=uname, email=email,
                                            password=pass1)
            user.save()
            messages.success(request, 'successfully register')
            return redirect('login')
    return render(request, 'register.html')

def login(request):                       #p2c-21-105
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('profile')
        else:
            messages.warning(request,'invalid credentials')
            return redirect('register')
    return render(request,'login.html')