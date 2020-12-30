from django.contrib.auth import authenticate, logout, login, get_user_model
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm
from .models import User
from django.contrib.auth.views import LoginView

User = get_user_model()

# Create your views here.
class SignView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = '/posts'


def logout_view(request):
    logout(request)
    return redirect('posts_archive')
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User.objects.create_user(full_name=full_name, password=password, email=email)
            new_user.set_password(form.cleaned_data['password'])
            return redirect('login')
        else:
            pass
        context = {'form': form}
    else:
        form = UserRegistrationForm()
        context = {'form': form}
    return render(request, 'blog/register.html', context=context)