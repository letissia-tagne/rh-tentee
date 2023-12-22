"""
URL configuration for authentification project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="authentification.index"),
    path('dashboard/', views.dashboard, name='authentification.dashboard'),
    path('utilisateurs/', views.utilisateurs, name='authentification.utilisateurs'),
    path("edit/<int:id>/", views.edit, name = "authentification.edit"),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view(), name='authentification.delete'),
    path('delete/<int:pk>/',views.delete, name='authentification.delete'),
    path('add/', views.add, name='authentification.add'),
    path('paies/', views.paies, name='authentification.paies'),
    path('disponibilites/', views.disponibilites, name='authentification.disponibilites'),
    path('parametres/', views.parametres, name='authentification.parametres'),
    path('edit_password/', views.edit_password, name='authentification.edit_password'),
    path('edit_infos/', views.edit_infos, name='authentification.edit_infos'),
    path('edit_password/', views.edit_password, name='authentification.edit_password'),
    path('presences_absences/',views.presences_absences, name='authentification.presences_absences'),
    path('conges/',views.conges, name='authentification.conges'),
    path('paie/', views.paie, name='authentification.payement'),
    path('disponibilite/conges', views.disponibilite_conges, name='authentification.disponibilite_conges'),
    path('user/', include('customuser.urls')),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
