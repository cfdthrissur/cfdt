from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['uname'], password=request.POST['passwd'])
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/home', {'current_user': request.user})
        else:
            return redirect('/login')
    else:
        return render(request, 'r2n2/login.html')

def home_page(request):
    return render(request, 'r2n2/index.html', {'current_user': request.user})
	
def logout_page(request):
	logout(request)
	return render(request, 'r2n2/login.html')
