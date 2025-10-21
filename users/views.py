from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        next_url = request.GET.get('next', '/admin/')

        return redirect(next_url)
    
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                next_url = request.GET.get('next', '/admin/')

                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)

    return redirect('login')
