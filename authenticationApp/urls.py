from django.urls import path
from authenticationApp.views import Index
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('profile', views.Profile, name='profile')
]