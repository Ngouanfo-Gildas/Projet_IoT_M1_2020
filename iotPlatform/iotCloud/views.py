from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .forms import *
from .models import *
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate

from iotCloud.models import Capteur
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class CapteurList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list.html'

    def get(self, request):
        queryset = Capteur.objects.all()
        return Response({'profiles': queryset})

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
    form_p = PuitsForm(request.POST or None)
    if request.method  == 'POST':
        reseau = Reseau()
        puits = Puits()
        user = User()
        propr = Proprietaire()
        if form.is_valid(): 
            nom_reseau = form.cleaned_data['nom_reseau']
            description_reseau = form.cleaned_data['description_reseau']
            reseau = form.save(commit=False)
            if user.is_authenticated:
                reseau.proprietaire_id = request.user.id
            
            key = datetime.datetime.now()
            reseau.network_key = "net"+key.strftime("%f%y%m%d%H%S")
            reseau.save()
            puits = form_p.save(commit=False)
            puits.reseau_id = reseau.id
            puits.sink_key = reseau.network_key
            puits.adresse = form_p.cleaned_data['adresse']
            puits.save()
            save = True
            return redirect('reseau_list')
    return render(request, 'iotCloud/nouveau_reseau.html', {'form':form, 'form_p':form_p })


@login_required(redirect_field_name='accounts/login')
def liste_reseau(request):
    user = User()
    reseaux = Reseau()
    nb = 0
    if user.is_authenticated:
        #reseau.proprietaire_id = request.user.id
        reseaux = Reseau.objects.filter(proprietaire_id = request.user.id)
    return render(request, 'iotCloud/reseau_list.html',  {'reseaux': reseaux})

@login_required(redirect_field_name='accounts/login')
def mon_profil(request):
    user = User()
    if user.is_authenticated:
        reseaux = Reseau.objects.filter(proprietaire_id = request.user.id)
        proprietaire = Proprietaire.objects.filter(user_id = request.user.id)
        #print(proprietaire.telephone_proprio)
    return render(request, 'iotCloud/votre_profil.html', {"reseaux": reseaux, "proprietaire": proprietaire})

def sensor_list(request, reseau_id):
    """ Cette fonction permet d'afficher la liste des 
        capteurs appartenant à au réseau dont l'id est:
        id_network """
    sensors = Capteur.objects.filter(reseau_id=reseau_id)
    return render(request, 'iotCloud/list.html', {'sensors':sensors})
    #path('network/<int:id>$', views.sensor_list, name='sensor_list'),
    #<a href="{% url 'sensor_list' id=sensor.reseau_id %}"></a>

def select_sensor_data(request, sensor_id):
    """ Afficher les données applicatives et de contrôles
        mesurées par le capteur d'id sensor_id """
    data_app = Donnee_appli.objects.filter(capteur_id=sensor_id)
    data_ctrl = Donnee_ctrl.objects.filter(capteur_id=sensor_id)
    return render(request, 'iotCloud/data_list.html', {'data_app':data_app, 'data_ctrl':data_ctrl })
    #path('network/list-data/<int:id>$', views.select_sensor_data, name='select_sensor_data'),
    #<a href="{% url 'select_sensor_data' id=sensor.id %}"></a>

def sensors_by_network(request, id_network):
    number_sensors = Capteur.objects.filter(reseau_id=id_network).count()
    return render(request, 'iotCloud/reseau_list.html', {'number_sensors':number_sensors})
    #path('network/<int:$', views.sensors_by_network, name='sensors_by_network'),
    #<a href="{% url 'sensors_by_network' id=sensor.reseau_id %}"></a>

def delete_network(request, id_network):
    network = Reseau.objects.filter(id=id_network).delete()
    return render(request, 'iotCloud/reseau_list.html', {'network':network})
    #path('network/<int:$', views.sensor_list, name='sensor_list'),
    #<a href="{% url 'delete_network' id=sensor.reseau_id %}"></a>

def edit_reseau(request):
    pass

def delete_reseau(request):
    pass



#pour le footer
def contact(request):
    return render(request, 'iotCloud/contact.html')

def conditions(request):
    return render(request, 'iotCloud/conditions.html')

def a_propos(request):
    return render(request, 'iotCloud/a_propos.html')

def aide(request):
    return render(request, 'iotCloud/aide.html')
    
def abonnement(request):
    return render(request, 'iotCloud/abonnement.html')
