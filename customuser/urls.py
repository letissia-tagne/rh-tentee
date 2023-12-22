from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="customuser.index"),
    path('register', views.customuser_register, name='customuser.register'),
    path('login', views.customuser_login, name='customuser.login'),
    path('logout', views.customuser_logout, name='customuser.logout'),
    path('add_utilisateur', views.add_utilisateur, name='customuser.add_utilisateur'),
]    
