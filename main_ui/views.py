from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import LogIssue
from .models import Issue
# Create your views here.

def index(response):
    ls = Issue.objects.all()
    if response.method == "POST":
        form = LogIssue(response.POST)
        if form.is_valid():
            iss_type = form.cleaned_data["issue_type"]
            desc = form.cleaned_data["issue_desc"]
            iss = Issue(
                issue_type=iss_type,
                issue_desc=desc,
                resolved=False,
                location_lat=0,
                location_long=0,
                )
            iss.save()
            return redirect(reverse("base"))
    else:
        form = LogIssue()
    return render(
        response,
        "main_ui/base.html",
        {
            "form": form,
            "ls": ls[::-1]
        })

