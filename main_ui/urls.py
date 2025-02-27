from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_issue, name="create_issue"),
    path("all_issues/", views.list_issues, name="list_issues"),
]