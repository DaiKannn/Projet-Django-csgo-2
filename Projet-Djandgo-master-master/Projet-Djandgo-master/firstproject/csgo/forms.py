from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CSGOForm(ModelForm):
    class Meta:
        model = models.CSGO
        fields = ('Nom_du_Major', 'Lieu', 'date_debut', 'date_fin', 'nombres_equipes','prix','resultat')
        labels = {
            'Nom_du_Major' : _('Major'),
            'Lieu' : _('Lieu') ,
            'date_debut' : _('date_debut'),
            'date_fin': _('date_fin'),
            'nombres_equipes' : _('nombres␣equipes'),
            'prix': _('Prix'),
            'resultat' : _('Resultat'),
        }

class MajorForm(ModelForm):
    class Meta:
        model = models.Major
        fields = ( 'tournoi','Nom','Maps_Jouées', 'Rating')
        labels = {
            'tournoi': _('tournoi'),
            'Nom': _('Nom'),
            'Maps_Jouées': _('Maps'),
            'Rating': _('Rating'),
        }
class CSGOInstantForm(ModelForm):
    class Meta:
        model = models.CSGO
        fields = ('Nom_du_Major', 'Lieu', 'date_debut', 'date_fin', 'nombres_equipes', 'prix','resultat')
        labels = {
            'Nom_du_Major': _('Major'),
            'Lieu': _('Lieu'),
            'date_debut': _('Date_debut'),
            'date_fin': _('Date_fin'),
            'nombres_equipes': _('Nombres␣equipes'),
            'prix': _('Prix'),
            'resultat': _('Resultat'),
        }
