from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(r'imageupload', views.home, name='home'),
    path(r'imageprocess',views.imageprocess, name='imageprocess'),
    
]
