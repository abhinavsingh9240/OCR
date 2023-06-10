import os

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from home import forms, models
from home.engine import get_text, get_boxes
from home.forms import UserRegistrationForm, DataForm
from home.models import Data
from ocr.settings import BASE_DIR


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return redirect("login")


def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':

        form = forms.LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect("home")  # not worked

            else:
                message = 'Login failed!'
    return render(
        request, 'login.html', context={'form': form, 'message': message})


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def logout_page(request):
    logout(request)
    return redirect("login")


def dashboard(request):
    if request.user.is_authenticated:
        img = None
        text = ""
        form = DataForm()
        if request.method == 'POST':
            form = DataForm(request.POST, request.FILES)

            if form.is_valid():
                # form.save()
                instance = form.save(commit=False)
                form = DataForm()
                instance.user = request.user
                instance.save()
                # print(instance.id)
                object_id = instance.id
                data_object = Data.objects.get(id=object_id)
                # print(data_object.image.url)
                # if instance.secondary_lang is None:
                #     language = instance.primary_lang
                # else:
                #     language = instance.primary_lang + "+" + instance.secondary_lang
                path = os.path.join(BASE_DIR,data_object.image.url[1:])
                text = get_text(path, language="ara+eng")
                instance.text = text
                instance.save()
                img = get_boxes(path, language="ara+eng")

        return render(request, 'dashboard.html', {'form': form, "text": text, "image": img})
    else:
        redirect("login")


def search(request):
    query = ""
    page_obj = []
    if request.method == "POST":
        query = request.POST.get("query")
        objects = Data.objects.filter(user=request.user).filter(text__icontains=query).order_by("-id")
        p = Paginator(objects, per_page=16)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)

    return render(request, 'search.html', {'page_obj': page_obj, "query": query})


def uploads(request):
    if request.user.is_authenticated:
        objects = Data.objects.filter(user=request.user).order_by("-id")
        p = Paginator(objects, per_page=16)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)
        context = {'page_obj': page_obj}
        return render(request, 'uploads.html', context)

    else:
        return redirect("login")


def delete(request, id=None):
    if request.user.is_authenticated:
        Data.objects.filter(user=request.user).filter(id=id).delete()

    return redirect("uploads")


def show(request, id):
    if request.user.is_authenticated:
        image_object = Data.objects.filter(user=request.user).get(id=id)
        return render(request, "show.html", {"object": image_object})
    else:
        redirect("login")


def settings(request):
    return render(request, "setttings.html")


def username(request):
    if request.method == "POST":
        form = forms.UsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            print()
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect("settings")

    else:
        form = forms.UsernameForm()

    context = {'form': form}
    return render(request, 'username.html', context)


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')


def name(request):
    if request.method == "POST":
        form = forms.NameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect("settings")

    else:
        form = forms.NameForm()

    context = {'form': form}
    return render(request, 'name.html', context)


def delete_user(request):
    User.objects.filter(id=request.user.id).delete()

    return redirect("home")
