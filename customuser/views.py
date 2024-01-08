from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .forms import CustomUserForm, RegisterChangeForm
from .models import CustomUser
from .models import Task

def index(request):
    users = CustomUser.objects.all()
    return render(request, 'customuser/index.html', {'users': users})

def customuser_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = CustomUser.objects.filter(username=username)

        if users.exists():
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Vous êtes maintenant connecté!')
                if user.is_superuser:
                    return redirect('authentification.dashboard')
                elif user.role in [2]:
                    return redirect('authentification.dashboard_rh')
                elif user.role == 1:
                     return redirect('authentification.dashboard_emp')
                else:
                    return redirect('authentification.index')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
                return redirect('customuser.login')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            return redirect('customuser.login')

    return render(request, 'customuser/login.html')


def customuser_logout(request):
    logout(request)
    messages.success(request, 'vous avez été deconnecter')
    return redirect('authentification.index')

def add_utilisateur(request):
    if request.method=="POST":
        username = request.POST.get('username')
        username = username.lower()
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        role = int(request.POST.get('role'))

        developpeur_group, created = Group.objects.get(name="Développeur")
        gestionnaire_rh_group, created = Group.objects.get(name="Gestionnaire RH")
        formateur_group, created = Group.objects.get(name="Formateur")
        chef_des_projets_group, created = Group.objects.get(name="Chef des projets")
        apprenant_group, created = Group.objects.get(name="Apprenant")
        
        
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(password)
            user.save()
            if role == 1:
                user.groups.add(developpeur_group)
            messages.success(request, 'Utilisateur ajouté avec succès.')
            
        elif role == 2:
                user.groups.add(gestionnaire_rh_group)
                messages.success
        elif role == 3:
                user.groups.add(formateur_group)
        elif role == 4:
                user.groups.add(chef_des_projets_group)
        elif role == 5:
                user.groups.add(apprenant_group)
        else: 
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            return redirect('authentification.add_utilisateur')


    return render('authentification/utilisateurs.html')


def ajouter_tache(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        date = request.POST.get('date')
        task = request.POST.get('task')
        duration = request.POST.get('duration')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
     
        user = request.user
        task = Task.objects.create(user=user, date=date, task=task, duration=duration, priority=priority, status=status)

        # Créer une nouvelle tâche
        Task.objects.create(date=date, task=task, duration=duration, priority=priority, status=status)
        
        # Rediriger vers la liste des tâches après l'ajout
        return redirect('authentification.taches')

    # Si la méthode n'est pas POST, afficher le formulaire d'ajout
    return render(request, 'authentification/taches.html')

#def create_view(request, *args, **kwargs):
#""""This view help to create and account for testing sending mails."""
#"""if request.method == "POST":
        # email = request.POST.get('email')
         #template ='email.html'"""