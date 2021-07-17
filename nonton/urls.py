from django.contrib import admin
from django.urls import path

from . import views

app_name = 'nonton'
urlpatterns = [
    path('', views.index, name="index"),
    path('post/<str:slugInput>/', views.detailPost, name='slug'),
    path('playlist/<str:playlistInput>/', views.playlistPost, name='playlist'),
]
