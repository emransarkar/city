from django.urls import path
from .views import view_map
from django.contrib.auth.views import LoginView, LogoutView
 
urlpatterns = [
    path('',view_map,name='view_map'),
]