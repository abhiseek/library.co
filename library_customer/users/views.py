from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from users.models import CustomUser
from django.http import HttpResponse

# Create your views here.


def adminregister(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,phone=n,address=a,is_superuser=True)
            u.save()
        else:
            return HttpResponse("passwords doesn't match")
        return redirect('users:login')
    return render(request, 'adminregister.html')

def userregister(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,phone=n,address=a,is_user=True)
            u.save()
        else:
            return HttpResponse("passwords doesn't match")
        return redirect('users:login')
    return render(request, 'register.html')


def login(request):
    if(request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            auth_login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("Invalid username or password.")
    return render(request, 'login.html')
@login_required
def logout(request):
    auth_logout(request)
    return redirect('users:login')


def home(request):
    return login(request)

def view_users(request):
    k=CustomUser.objects.all()
    return render(request, 'userdetail.html', {'user': k})