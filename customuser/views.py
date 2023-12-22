from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .forms import CustomUserForm, RegisterChangeForm
from .models import CustomUser

def index(request):
    users = CustomUser.objects.all()
    return render(request, 'customuser/index.html', {'users': users})


def customuser_register(request):
    if request.method=="POST":
      print(request.POST)
      username= request.POST.get('username')
      email=   request.POST.get('email')
      password= request.POST.get('password')
      password1= request.POST.get('password1')

      if CustomUser.objects.filter(username=username):
          messages.error(request, 'ce nom  a ete deja pri')
          return redirect('customuser.register')
        
      
      if CustomUser.objects.filter(email=email):
          messages.error(request, 'cet email a deja un compte')
          return redirect('customuser.register')
      
      if not username.isalnum():
          messages.error(request, 'le nom doit etre alphanumérique')
          return redirect('customuser.register')
      
      if password != password1:
          #hascher le mot de passe 
          messages.error(request, 'les deux passwords ne coincident pas ')
          return redirect('customuser.register')
      
      form = RegisterChangeForm(request.POST)
      if form.is_valid():
        form.save()
        user = CustomUser.objects.get(username=username)
        user.set_password(password)
        user.save()
        messages.success(request, 'votre compte a ete crée avec success.')
      return redirect('customuser.login')
    return render(request, 'customuser/register.html')



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
        
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(password)
            user.save()

    return redirect('authentification.utilisateurs')
