from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import LogIssue
from .models import Issue
# Create your views here.

def list_issues(response):
    issues = Issue.objects.all()
    if response.method == "POST":
        if response.POST.get("Create") == "goto":
            return redirect(reverse("create_issue"))
    return render(
        response,
        "main_ui/list_issues.html",
        {
            "issues": issues,
        })


def create_issue(response):
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
            return redirect(reverse("create_issue"))
    else:
        form = LogIssue()
    return render(
        response,
        "main_ui/create_issue.html",
        {
            "form": form,
        })

