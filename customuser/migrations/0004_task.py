# Generated by Django 4.2.7 on 2024-01-05 15:43

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('task', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('priority', models.CharField(choices=[('Haute', 'Haute'), ('Moyenne', 'Moyenne'), ('Basse', 'Basse')], max_length=10)),
                ('status', models.CharField(choices=[('En cours', 'En cours'), ('Terminé', 'Terminé'), ('En attente', 'En attente')], max_length=10)),
            ],
        ),
    ]
