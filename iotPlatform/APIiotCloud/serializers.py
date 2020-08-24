from rest_framework import serializers
from iotCloud.models import (
    Reseau, 
    Puits, 
    Capteur,
    Etat_capteur, 
    Service, 
    Souscription, 
    Donnee_ctrl, 
    Donnee_appli,
)

class ReseauSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Reseau 
        fields = ('nom_reseau', 'network_key', 'date_creation', 'description_reseau')

class PuitsSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Puits
        fields = ('reseau', 'adresse', 'sink_key')

class CapteurSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Capteur
        fields = ('reseau', 'nom_capteur', 'adresse_capteur', 'description_capteur')

class Donnee_appliSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Donnee_appli
        fields = ('capteur', 'valeur_brute', 'valeur_traite', 'date', 'heure')

class Donnee_ctrlSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Donnee_ctrl
        fields = ('capteur', 'taux_livraison', 'qlte_signal', 'date', 'heure', 'voisin')

class SouscriptionSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Souscription
        fields = ('reseau', 'proprietaire', 'service', 'date_sous')

class ServiceSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Service
        fields = ('nom', 'description', 'duree', 'cout')

class Etat_capteurSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Etat_capteur
        fields = ('capteur',  'energie', 'date', 'heure')
