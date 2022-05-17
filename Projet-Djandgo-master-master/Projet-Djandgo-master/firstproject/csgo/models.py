from django.db import models


class CSGO(models.Model):
    Nom_du_Major = models.CharField(max_length=100)
    Lieu = models.CharField(max_length=100)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    nombres_equipes = models.IntegerField(blank=False)
    prix = models.CharField(max_length=100,default="100")
    resultat = models.CharField(max_length=100,default="toto")

    def __str__(self):
        chaine = f" Voici le major {self.Nom_du_Major} qui a eu lieu {self.Lieu} entre le {self.date_debut} et le {self.date_fin} avec {self.nombres_equipes} .Le cash prize etait de {self.prix}.  {self.resultat}"
        return chaine

    def dico(self):
        return {"Nom_du_Major": self.Nom_du_Major, "Lieu": self.Lieu, "date_debut": self.date_debut, "date_fin": self.date_fin,
                "nombres_equipes": self.nombres_equipes, "prix": self.prix, "resultat": self.resultat}


class Major(models.Model):
    tournoi = models.CharField(max_length=100,default="toto")
    Nom = models.CharField(max_length=100)
    Maps_Jouées = models.IntegerField(blank=False)
    Rating = models.IntegerField(blank=False)


    def __str__(self):
        chaine = f"{self.tournoi} fefef {self.Nom} le resultat {self.Maps_Jouées} voici les stats des joueurs {self.Rating}"
        return chaine

    def dico(self):
        return {"tournoi": self.tournoi,"Nom": self.Nom, "Maps_Jouées": self.Maps_Jouées,
                "Rating": self.Rating}