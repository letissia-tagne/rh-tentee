from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(_("User name"),  max_length=255, unique=True)
    position = models.CharField(max_length=100,default='')
    date_of_hire = models.DateField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=100,default='')
    ROLES = (
        (1, 'Développeur'),
        (2, 'Gestionnaire RH'),
        (3, 'Formateur'),
        (4, 'Chef des projets'),
        (5, 'Apprenant'),
    )
    role = models.PositiveIntegerField(default=None, null=True, blank=True, choices=ROLES)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    date = models.DateField()
    task = models.CharField(max_length=255)
    duration = models.IntegerField()
    priority = models.CharField(max_length=10, choices=[('Haute', 'Haute'), ('Moyenne', 'Moyenne'), ('Basse', 'Basse')])
    status = models.CharField(max_length=10, choices=[('En cours', 'En cours'), ('Terminé', 'Terminé'), ('En attente', 'En attente')])