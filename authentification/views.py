from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import get_user_model
from django.contrib import messages 
from django.shortcuts import render
from django.shortcuts import render, redirect
from customuser.forms import CustomUserForm, RegisterChangeForm
from customuser.models import CustomUser
from django.views.generic import DeleteView
from django.urls import reverse_lazy



def index(request):
    if request.user.is_authenticated and (request.user.is_superuser or request.user.role == 2):
        return redirect('authentification.dashboard')
    return render(request,'authentification/index.html')

def dashboard(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        if request.user.role == 2:
            return redirect('authentification.dashboard_rh')
        return redirect('authentification.index')
    return render(request, 'authentification/dashboard.html')

def dashboard_rh(request):
    if not request.user.is_authenticated or not request.user.role == 2:
        return redirect('authentification.index')
    return render(request, 'authentification/dashboard_rh.html')

def dashboard_emp(request):
    if not request.user.is_authenticated or not request.user.role == 1:
        return redirect('authentification.index')
    return render(request, 'authentification/dashboard_emp.html')

def utilisateurs(request):
    users = CustomUser.objects.filter(is_superuser=False)
    return render (request, 'authentification/utilisateurs.html', {'users': users})

def paie(request):
    return render(request, 'authentification/paie.html')

def disponibilite(request):
    return render(request, 'authentification/disponibilite.html')

def parametres(request):
    return render(request, 'authentification/parametres.html')

def paies(request):
    return render(request, 'authentification/paies.html')

def disponibilites(request):
    return render(request, 'authentification/disponibilites.html')

def presences_absences(request):
    return render(request, 'authentification/presences_absences.html')

def conges(request):
    return render (request, 'authentification/conges.html')

def disponibilite_conges(request):
    return render(request, 'authentification/conges.html')

def add(request):
    return render(request, 'authentification/utilisateurs.html')

def edit_infos(request):
    return render(request, 'authentification/edit_infos.html')
  
def edit_password(request):
    return render(request, 'authentification/edit_password.html') 

def edit(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method=="POST":
        username = request.POST.get('username')
        username = username.lower()
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('authentification.utilisateurs')

    return render(request, "authentification/edit.html", {'user': user})

class UserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('utilisateurs')
    template_name = 'authentification/delete.html'
    pk_url_kwarg = 'pk' 
    
def delete(request,pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request,'cet utilisateur a ete supprimer avec succes')
        return redirect('authentification.utilisateurs')
    return render(request,"authentification/delete.html", {'object': user})
 
 # views.py
from django.shortcuts import render

def recherche(request):
    query = request.GET.get('q')
    resultats = CustomUser.objects.filter(username__icontains=query)
    return render(request, 'authentification/resultats_recherche.html', {'resultats': resultats})

        
        
def delete_rh(request):
    return render(request, 'authentification/utilisateurs_rh.html')


from django.shortcuts import render

def search_results(request):
    resultats = {'resultat1': 'valeur1', 'resultat2': 'valeur2', 'resultat3': 'valeur3'}  # Exemple de données
    return render(request, 'authentification/resultats_recherche.html', {'resultats': resultats})

def listes_rh(request):
    return render( request, "authentification/listes_rh.html")

def absences_rh(request):
    return render(request, "authentification/absences_rh.html")

def conges_rh(request):
    return render(request, "authentification/conges_rh.html")

def suivi_horaire(request):
    return render(request, "authentification/suivi_horaire.html")

def contrat_attes(request):
    return render (request,"authentification/contrat_attes.html")

def groupes(request):
    return render(request,'authentification/groupes.html')

def taches(request):
    return render(request, 'authentification/taches.html')

def ajouter_tache(request):
    return render(request, 'authentification/taches.html')