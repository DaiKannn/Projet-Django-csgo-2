# Generated by Django 4.0.4 on 2022-05-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csgo', '0005_rename_equipe_major_maps_jouées_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='tournoi',
            field=models.CharField(default='toto', max_length=100),
        ),
        migrations.AlterField(
            model_name='csgo',
            name='prix',
            field=models.CharField(default='100', max_length=100),
        ),
        migrations.AlterField(
            model_name='csgo',
            name='resultat',
            field=models.CharField(default='toto', max_length=100),
        ),
        migrations.AlterField(
            model_name='major',
            name='Maps_Jouées',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='major',
            name='Nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='major',
            name='Rating',
            field=models.IntegerField(),
        ),
    ]