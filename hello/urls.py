from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main),
    path('hello/', views.Hello),
]
