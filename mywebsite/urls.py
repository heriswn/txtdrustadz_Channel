from django.contrib import admin
from django.urls import path , include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls', namespace='about')),
    path('nonton/', include('nonton.urls', namespace='nonton')),
    path('form/', include('form.urls', namespace='form')),
    path('', views.index, name="index"),
]
