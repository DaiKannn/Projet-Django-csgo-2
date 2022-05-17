from django.urls import path
from . import views
urlpatterns = [
    path('accueilcsgo/', views.accueilcsgo),
    path('formulairecsgo/', views.formulairecsgo, name='formulaire'),
    path('traitementcsgo/', views.traitementcsgo),
    path("affichecsgo/",views.affichecsgo),
    path("updatecsgo/<int:id>/",views.updatecsgo),
    path("updatetraitementcsgo/<int:id>/",views.updatetraitementcsgo),
    path("deletecsgo/<int:id>/",  views.deletecsgo),
    path("formulairemajor/", views.formulairemajor),
    path("affichemajor/", views.affichemajor),
    path ("traitementmajor/", views.traitementmajor),
    path("updatemajor/<int:id>/", views.updatemajor),
    path("updatetraitementmajor/<int:id>/", views.updatetraitementmajor),
    path ("deletemajor/<int:id>/", views.deletemajor),
    path('traitementinstantcsgo/<int:id>/', views.traitementinstantcsgo),
    path('formulaireinstantcsgo/<int:id>/', views.formulaireinstantcsgo),

]