import asyncio
from typing import Optional

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest

from walker.common_functions import send_email, save_proxies
from walker.forms import SignUpForm, TaskForm, ProxyForm
from walker.models import Proxy, Task


@login_required(login_url='/sign-in/')
def index(request: WSGIRequest):
    tasks = Task.objects.filter(owner=request.user.id)
    return render(request, 'walker/index.html', {'tasks': tasks})


@login_required(login_url='/sign-in/')
def task_page(request: WSGIRequest, task_id: Optional[int] = None):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            task.name = f"Задача {task.id}"
            task.save()
            return redirect('/')

        return render(request, 'walker/task.html', {'form': form})
    else:
        if task_id:
            task = Task.objects.get(pk=task_id)
            return render(request, 'walker/task.html', {'form': TaskForm(instance=task)})
        return render(request, 'walker/task.html', {'form': TaskForm()})


@login_required(login_url='/sign-in/')
def remove_task(request: WSGIRequest, task_id: int):
    Task.objects.get(pk=task_id).delete()
    return redirect('/')


@login_required(login_url='/sign-in/')
def change_task_status(request: WSGIRequest, task_id: int):
    task = Task.objects.get(pk=task_id)
    if task.status:
        task.status = False
    else:
        task.status = True
    task.save()
    return redirect('/')


def settings(request: WSGIRequest):
    if request.method == 'POST':
        proxy_field_text = request.POST['proxies']
        Proxy.objects.filter(owner=request.user).delete()
        asyncio.run(save_proxies(user=request.user, text_data=proxy_field_text))

    proxies = Proxy.objects.filter(owner=request.user)
    proxy_list = [f"{p.host}:{p.port}:{p.username}:{p.password}" for p in proxies]
    proxy_form = ProxyForm(initial={'proxies': '\n'.join(proxy_list)})
    return render(request, 'walker/settings.html', {'proxy_form': proxy_form})


def sign_up(request: WSGIRequest):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # send_email(email, username, raw_password)
            return redirect('/')
        else:
            return render(request, 'walker/sign-up.html', {'form_error': form})
    else:
        form = SignUpForm()
    return render(request, 'walker/sign-up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not request.user.is_authenticated:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return redirect('/sign-up/')
        return redirect('/')
    return render(request, 'walker/sign-in.html', {'form': AuthenticationForm()})


def sign_out(request):
    logout(request)
    return redirect('/')
