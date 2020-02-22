from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    # path('login', views.login),
    path('signup', views.signup),
    path('register', views.customRegister),
    path('login', views.handleLogin),
    path('logout', views.handleLogout),
]