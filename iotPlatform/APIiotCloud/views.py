from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST

from rest_framework import viewsets, permissions

from .serializers import (
    ReseauSerializer, 
    PuitsSerializer, 
    CapteurSerializer,
    ServiceSerializer
)
from iotCloud.models import (
    Reseau, 
    Capteur, 
    Puits, 
    Service, 
    Souscription, 
    Donnee_appli,
    Donnee_ctrl,
    Etat_capteur
)

############################################

"""@define_usage(params={'username': 'String', 'password': 'String'},
               returns={'authenticated': 'Bool', 'token': 'Token String'})"""
@api_view(['POST'])
@permission_classes((AllowAny,))
def api_signin(request):
    try:
        username = request.data['username']
        password = request.data['password']
    except:
        return Response({'error': 'Please provide correct username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'authenticated': True, 'token': "Token " + token.key})
    else:
        return Response({'authenticated': False, 'token': None})

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

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

##############################################
import json 


#URL /new/
#@define_usage(params={'description': 'String', 'due_in': 'Int'},
            #returns={'done': 'Bool'})
@api_view(['POST'])
#@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
#@permission_classes((IsAuthenticated,))
def api_new_DAPP(request):    
    donnee_appli = request
    data = json.loads(donnee_appli)
    operation = data['operation']
    
    network_id = data['networkID']
    sink_id = data['sinkID']
    indice = 0
    while indice<len(data['sensors']):
        sensor=data['sensors']
        id_s       = sensor[indice]['id']
        addr_s     = sensor[indice]['address']
        desc_s     = sensor[indice]['description']
        data_type  = sensor[indice]['datas']['type']
        data_valeur= sensor[indice]['datas']['valeur']
        data_unit  = sensor[indice]['datas']['unite']
    
    network = Reseau.objects.filter(id=network_id)
    sink    = Puits.objects.filter(id=sink_id)
    if network is not None:
        if sink is not None:
            sensor_ = Capteur(
                reseau = request.data['network_id'],
                nom_capteur = 'cap1', #request.data['cap1'],
                adresse_capteur = request.data['addr_s'],
                description_capteur = request.data['desc_s'],
            )
            sensor.save()
    return Response({'done': True})

