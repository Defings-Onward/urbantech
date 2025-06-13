from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('portfolio/<int:id>', views.details, name="portfolio")
]