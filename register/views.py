from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            redirect(reverse("login"))
        
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
