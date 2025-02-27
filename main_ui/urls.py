from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_issue, name="create_issue"),
    path("all_issues/", views.list_issues, name="list_issues"),
    path("logout_confirm/", views.logout, name="logout"),
    path("test/", views.test, name="test"),
]