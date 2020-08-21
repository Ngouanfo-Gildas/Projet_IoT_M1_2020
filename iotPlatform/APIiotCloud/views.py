from rest_framework import viewsets, permissions

from .serializers import ReseauSerializer, PuitsSerializer, CapteurSerializer
from iotCloud.models import Reseau, Capteur, Puits

################

class ReseauViewSet(viewsets.ModelViewSet):
    queryset = Reseau.objects.all()
    serializer_class = ReseauSerializer

class PuitsViewSet(viewsets.ModelViewSet):
    queryset = Puits.objects.all()
    serializer_class = PuitsSerializer

class CapteurViewSet(viewsets.ModelViewSet):
    queryset = Capteur.objects.all()#.order_by('name')
    serializer_class = CapteurSerializer

##############################################
