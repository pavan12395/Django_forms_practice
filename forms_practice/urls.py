
from django.contrib import admin
from django.urls import path
from .views import loginView,loggedView,sessionloginView,sessionloggedView,sessionLogoutView
urlpatterns = [
    path('login/',loginView),
    path('logged/',loggedView),
    path('sessionlogin/',sessionloginView),
    path('sessionlogged/',sessionloggedView),
    path('sessionLogout/',sessionLogoutView)
]
