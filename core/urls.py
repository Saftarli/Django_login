from enum import verify

from django.urls import path
from django.views.generic import detail

from core.views import index, register, login_user, logout,verify

urlpatterns = [
        path('', index, name='home'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout, name='logout'),
        path('verify_email/<uidb64>/<token>/', verify, name='verify_email'),
]