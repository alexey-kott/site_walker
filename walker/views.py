from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest

from walker.common_functions import send_email
from walker.models import ProxyModel


@login_required(login_url='/sign-in/')
def index(request):
    proxies = ProxyModel.objects.filter(owner=1)
    return render(request, 'walker/index.html', {'proxies': proxies})


def sign_up(request: WSGIRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # send_email(email, username, raw_password)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'walker/sign-up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        if not request.user.is_authenticated:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return redirect('/sign-up/')
        return redirect('/')
    return render(request, 'walker/sign-in.html', {})


def sign_out(request):
    logout(request)
    return redirect('/')
