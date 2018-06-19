from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['uname'], password=request.POST['passwd'])
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/login?e=1')
    else:
        return render(request, 'r2n2/login.html')

def home_page(request):
    return render(request, 'r2n2/index.html')
