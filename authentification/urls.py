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
    path('dashboard_rh/', views.dashboard_rh, name='authentification.dashboard_rh'),
    path('dashboard_emp/',views.dashboard_emp, name='authentification.dashboard_emp'),
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
    path('recherche/', views.recherche, name='authentification.resultats_recherche'),
    path('listes_rh/', views.listes_rh, name='authentification.listes_rh'),
    path('absences_rh/',views.absences_rh, name='authentification.absences_rh'),
    path('conges_rh/', views.conges_rh, name='authentification.conges_rh'),
    path('suivi_horaire/', views.suivi_horaire, name='authentification.suivi_horaire'),
    path('contrat_attes/', views.contrat_attes, name='authentification.contrat_attes'),
    path('groupes/', views.groupes, name='authentification.groupes'),
    path('taches/', views.taches, name='authentification.taches'),
    path('ajouter_tache/', views.ajouter_tache, name='authentification.ajouter_tache')

]   

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
