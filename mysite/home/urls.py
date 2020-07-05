from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

app_name = 'home'
urlpatterns = [
path('', TemplateView.as_view(template_name='home/main.html')),
path('cookie', views.cookie),
path('hello', views.hello),
path('polls/',include('polls.urls')),
# path('/',include('polls.urls')),
]