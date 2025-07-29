from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    print(request.user.username)
    return render(request, 'login.html')


def signupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        name = request.POST.get('name')
        age = request.POST.get('age')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same")
        else:
            if User.objects.filter(username=uname).exists():
                return HttpResponse("Username already exists, please choose another username.")
            try:
                my_user = User.objects.create_user(uname, email, pass1)
                print('User created:', my_user)
                print('Name:', name)
                print('Age:', age)
                my_user.save()
                return redirect('login')
            except Exception as e:
                return HttpResponse("An error occurred. Please try again.")
    return render(request, 'signup.html')


def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('superadmin_dashboard')
            elif user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            return HttpResponse("Invalid username and/or password.")
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


# def profile(request):
#     return render(request, 'profile.html')
