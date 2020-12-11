from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from .models import User


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('posts_archive')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('posts_archive')
    else:
        pass
    return render(request, 'blog/login.html', context={})


def logout_view(request):
    logout(request)
    return redirect('posts_archive')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, first_name=first_name,
                                     last_name=last_name, email=email)

            return redirect('login')
        else:
            pass
        context = {'form': form}
    else:
        form = UserRegistrationForm()
        context = {'form': form}
    return render(request, 'blog/register.html', context=context)
