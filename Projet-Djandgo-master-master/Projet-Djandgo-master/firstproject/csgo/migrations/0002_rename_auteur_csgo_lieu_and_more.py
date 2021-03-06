# Generated by Django 4.0.4 on 2022-05-16 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csgo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csgo',
            old_name='auteur',
            new_name='Lieu',
        ),
        migrations.RenameField(
            model_name='csgo',
            old_name='date_parution',
            new_name='dates',
        ),
        migrations.RenameField(
            model_name='csgo',
            old_name='nombres_pages',
            new_name='nombres_equipes',
        ),
        migrations.RenameField(
            model_name='csgo',
            old_name='resume',
            new_name='resultat',
        ),
        migrations.RenameField(
            model_name='major',
            old_name='Region',
            new_name='Equipe',
        ),
        migrations.RenameField(
            model_name='major',
            old_name='Universite',
            new_name='Horaire',
        ),
        migrations.RenameField(
            model_name='major',
            old_name='Departement',
            new_name='Score',
        ),
        migrations.RenameField(
            model_name='major',
            old_name='nombres_de_livres',
            new_name='Stats',
        ),
        migrations.RemoveField(
            model_name='csgo',
            name='bibliotheque',
        ),
    ]
