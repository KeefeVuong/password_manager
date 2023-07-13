from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Account
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def accounts(request):
    myaccounts = Account.objects.filter(owner=request.user).values()
    context = {
        'myaccounts': myaccounts
    }
    return render(request, "all_accounts.html", context)

@login_required(login_url="/login/")
def details(request, id):
    myaccount = Account.objects.get(id=id)
    context = {
        'myaccount': myaccount,
    }
    return render(request, "details.html", context)

def main(request):
    return render(request, "main.html", {'request': request})

@login_required(login_url="/login/")
def create(request):
    if request.method == "POST":
        platform = request.POST.get("platform_input")
        username = request.POST.get("username_input")
        password = request.POST.get("password_input")
        
        account = Account(owner=request.user, platform=platform, username=username, password=password)
        account.save()

    return render(request, "create.html", {})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("/accounts")
    else:
        form = RegisterForm()

    return render(request, "register.html", {'form': form})