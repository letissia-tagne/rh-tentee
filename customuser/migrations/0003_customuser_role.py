# Generated by Django 4.2.7 on 2023-12-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_customuser_address_customuser_date_of_hire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Développeur'), (2, 'Gestionnaire RH'), (3, 'Formateur'), (4, 'Chef des projets'), (5, 'Apprenant')], default=None, null=True),
        ),
    ]
