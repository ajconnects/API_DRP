from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.Home_page),
    path("demo-version/", views.demo_version),
]