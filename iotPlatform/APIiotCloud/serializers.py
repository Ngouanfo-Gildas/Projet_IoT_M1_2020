from rest_framework import serializers
from iotCloud.models import Reseau, Puits, Capteur

class ReseauSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Reseau 
        fields = ('nom_reseau', 'date_creation', 'description_reseau')

class PuitsSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Puits
        fields = ('reseau', 'adresse')

class CapteurSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Capteur
        fields = ('reseau', 'nom_capteur', 'adresse_capteur', 'description_capteur')

