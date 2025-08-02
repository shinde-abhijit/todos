from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('user-logout/', views.user_logout, name='user_logout'),
    path('user-register/', views.user_register, name='user_register'),
]
