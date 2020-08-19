from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.contrib.auth import authenticate , logout

############################################################################################
##########            gestion des réseaux; capteurs et des données                ##########
#############----------------------------------------------------------------###############


def home(request):
    return render(request, 'iotCloud/accueil.html', locals())

def home1(request):
    return render(request, 'iotCloud/accueil1.html', locals())


@login_required(redirect_field_name='accounts/login')
def nouveau_reseau(request):
    save = False
    form = ReseauForm(request.POST or None)
    if request.method  == 'POST':
        reseau = Reseau()
        user = User()
        propr = Proprietaire()
        if form.is_valid(): 
            nom_reseau = form.cleaned_data['nom_reseau']
            description_reseau = form.cleaned_data['description_reseau']
            
            reseau = form.save(commit=False)
            if user.is_authenticated:
                reseau.proprietaire_id = request.user.id
            #reseau.proprietaire_id = 1 #Proprietaire.objects.filter(user = 1)
            
            reseau.save()
            save = True
            return redirect('reseau_list')
    return render(request, 'gestionIoT/nouveau_reseau.html', {'form':form })

@login_required(redirect_field_name='accounts/login')
def liste_reseau(request):
    user = User()
    reseau = Reseau()
    nb = 0
    if user.is_authenticated:
        #reseau.proprietaire_id = request.user.id
        reseaux = Reseau.objects.filter(proprietaire_id = request.user.id)
        
    return render(request, 'iotCloud/reseau_list.html', {'reseaux': reseaux, "nb": nb}) #locals())

@login_required(redirect_field_name='connexion')
def mon_profil(request):
    user = User()
    if user.is_authenticated:
        reseaux = Reseau.objects.filter(proprietaire_id = request.user.id)
        proprietaire = Proprietaire.objects.filter(user_id = request.user.id)
        #print(proprietaire.telephone_proprio)
    return render(request, 'iotCloud/votre_profil.html', {"reseaux": reseaux, "proprietaire": proprietaire})



def nouveau_puits(request):
    pass

def edit_reseau(request):
    pass

def delete_reseau(request):
    pass


