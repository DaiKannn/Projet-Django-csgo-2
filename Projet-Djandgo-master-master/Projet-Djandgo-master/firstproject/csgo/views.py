from django.shortcuts import render, HttpResponseRedirect
from .forms import CSGOForm, MajorForm, CSGOInstantForm
from . import models



def accueilcsgo(request):
    liste = list(models.CSGO.objects.all())
    return render(request, "csgo/accueilcsgo.html", {"liste": liste})

def formulairecsgo(request):
    if request.method == "POST":
        form = CSGOForm(request)
        return render(request, 'csgo/formulairecsgo.html', {'form': form})
    else:
        form = CSGOForm()
        return render(request, 'csgo/formulairecsgo.html', {'form': form})


def traitementcsgo(request):
    pForm = CSGOForm(request.POST)
    if pForm.is_valid():
        Csgo = pForm.save()
        return HttpResponseRedirect("/csgo/accueilcsgo")
    else:
        return render(request, 'csgo/traitementcsgo.html', {'form': pForm})

def affichecsgo(request):
    csgo = models.CSGO.objects.all()
    allmajor = models.CSGO.objects.all()
    return render(request, "csgo/affichecsgo.html", {"csgo": csgo, "allmajor": allmajor})




def updatecsgo(request, id):
     CSGO = models.CSGO.objects.get(pk=id)
     form = CSGOForm(CSGO.dico())
     return render(request, "csgo/formulairecsgo.html", {"form": form, "id": id})


def updatetraitementcsgo(request, id):
     pform = CSGOForm(request.POST)
     if pform.is_valid():
         CSGO = pform.save(commit=False)
         CSGO.id = id
         CSGO.save()
         return HttpResponseRedirect("/csgo/accueilcsgo")
     else:
         return render(request, "csgo/formulairecsgo.html", {"form": pform, "id": id})


def deletecsgo(request, id):
     CSGO = models.CSGO.objects.get(pk=id)
     CSGO.delete()
     return HttpResponseRedirect("/csgo/accueilcsgo")

def formulaireinstantcsgo(request, id):
    form = CSGOInstantForm()
    return render(request, 'csgo/formulaireinstantcsgo.html', {'form': form, "id": id})


def traitementinstantcsgo(request, id):
     if request.method == "POST":
         pForm = CSGOInstantForm(request.POST)
         if pForm.is_valid():
             csgo = pForm.save(commit=False)
             csgo.major_id = id
             csgo.major = models.CSGO.objects.get(pk=id)
             csgo.save()
             return render(request, 'csgo/traitementinstantcsgo.html', {'csgo': csgo, "id": id})
         else:
             return render(request, 'csgo/formulaireinstantcsgo.html', {'form': pForm, "id": id})

def affichemajor(request):
    major = models.Major.objects.all()
    allmvp = models.Major.objects.all()
    return render(request, "Major/affichemajor.html", {"major": major, "allmvp": allmvp})


def formulairemajor(request):
     if request.method == "POST":
         form = MajorForm(request)
         return render(request, 'Major/formulairemajor.html', {'form': form})
     else:
         form = MajorForm()
         return render(request, 'Major/formulairemajor.html', {'form': form})

def traitementmajor(request):
     pForm = MajorForm(request.POST)
     if pForm.is_valid():
         Major = pForm.save()
         return HttpResponseRedirect(f"/csgo/affichemajor/{Major.id}/")
     else:
         return render(request, 'Major/traitementmajor.html', {'form': pForm})


def updatemajor(request, id):
     Major = models.Major.objects.get(pk=id)
     form = MajorForm(Major.dico())
     return render(request, "Major/formulairemajor.html", {"form": form, "id": id})


def updatetraitementmajor(request, id):
     pform = MajorForm(request.POST)
     if pform.is_valid():
         Major = pform.save(commit=False)
         Major.id = id
         Major.save()
         return HttpResponseRedirect("/csgo/")
     else:
         return render(request, "Major/formulairemajor.html", {"form": pform, "id": id})


def deletemajor(request, id):
     major = models.Major.objects.get(pk=id)
     major.delete()
     return HttpResponseRedirect("/csgo/accueilmajor")


