from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.Home_page),
    path("demo-version/", views.demo_version),
    path('custom-version/', views.DemoView.as_view()),
    path('another-custom-version/', views.AnotherView.as_view()),
]