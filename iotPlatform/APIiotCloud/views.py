from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST
# More rest imports as needed
from django.contrib.auth import authenticate
from datetime import date, timedelta
from .decorators import define_usage

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
#URL /signin/
#Note that in a real Django project, signin and signup would most likely be
#handled by a seperate app. For signup on this example, use the admin panel.
@define_usage(params={'username': 'String', 'password': 'String'},
                returns={'authenticated': 'Bool', 'token': 'Token String'})
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

@define_usage(params={'description': 'String', 'due_in': 'Int'},
            returns={'done': 'Bool'})
@api_view(['PUT'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def api_new_DAPP(request):
    try:    
        network = Reseau.objects.get(network_key=request.data['network_key'])
    except Reseau.DoesNotExist:
        network = None
    try:
        sink    = Puits.objects.get(sink_key=request.data['sink_key'])
    except Puits.DoesNotExist:
        sink = None
    if network is not None:
        print('net exist')
        if sink is not None:
            i = 0    #compteur de capteur
            while i<len(request.data['sensors']):
                if sink.sink_key == network.network_key:
                    try:
                        sensor_t = Capteur.objects.get(adresse_capteur=request.data['sensors'][i]['sensor_address'])
                    except Capteur.DoesNotExist:
                        sensor_t = None
                    print("\n\ntoto\n")
                    if sensor_t is None:
                        sensor = Capteur(
                                nom_capteur = request.data['sensors'][i]['sensor_name'],
                                adresse_capteur = request.data['sensors'][i]['sensor_address'],
                                description_capteur = request.data['sensors'][i]['sensor_description'],
                                reseau_id = network.id
                            )
                        sensor.save()

                    data_app = Donnee_appli(
                        valeur_brute  = request.data['sensors'][i]['datas']['valeur'],
                        valeur_traite = request.data['sensors'][i]['datas']['valeur'],
                        type_data  = request.data['sensors'][i]['datas']['type'],
                        unity_data = request.data['sensors'][i]['datas']['unite'],
                        capteur_id = sensor_t.id if sensor_t is not None else sensor.id
                    )
                    data_app.save()
                else:
                    pass
                i += 1
        else:
            pass
    return Response({'done': True})
    

@define_usage(params={'description': 'String', 'due_in': 'Int'},
            returns={'done': 'Bool'})
@api_view(['PUT'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def api_new_DCTRL(request):
    try:    
        network = Reseau.objects.get(network_key=request.data['network_key'])
    except Reseau.DoesNotExist:
        network = None
    try:
        sink    = Puits.objects.get(sink_key=request.data['sink_key'])
    except Puits.DoesNotExist:
        sink = None
    if network is not None:
        if sink is not None:
            i = 0    #compteur de capteur
            while i<len(request.data['sensors']):
                if sink.sink_key == network.network_key:
                    try:
                        sensor_t = Capteur.objects.get(adresse_capteur=request.data['sensors'][i]['sensor_address'])
                    except Capteur.DoesNotExist:
                        sensor_t = None
                    if sensor_t is None:
                        sensor = Capteur(
                                nom_capteur = request.data['sensors'][i]['sensor_name'],
                                adresse_capteur = request.data['sensors'][i]['sensor_address'],
                                description_capteur = request.data['sensors'][i]['sensor_description'],
                                reseau_id = network.id
                            )
                        sensor.save()

                    data_ctrl = Donnee_ctrl(
                        lq  = request.data['sensors'][i]['datas']['lq'],
                        rssi = request.data['sensors'][i]['datas']['rssi'],
                        voisin  = request.data['sensors'][i]['datas']['voisin'],
                        capteur_id = sensor_t.id if sensor_t is not None else sensor.id
                    )
                    data_ctrl.save()
                    state_sensor = Etat_capteur(
                        energie  = request.data['sensors'][i]['etat']['energie'],
                        capteur_id = sensor_t.id if sensor_t is not None else sensor.id
                    )
                    state_sensor.save()
                else:
                    pass
                i += 1 #next sensor
            else:
                pass
    return Response({'done': True})

@define_usage(params={'description': 'String', 'due_in': 'Int'},
            returns={'done': 'Bool'})
@api_view(['PUT'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def add_data(request):
    if request.data['operation'] == "addAppData":
        try:    
            network = Reseau.objects.get(network_key=request.data['network_key'])
        except Reseau.DoesNotExist:
            network = None
        try:
            sink    = Puits.objects.get(sink_key=request.data['sink_key'])
        except Puits.DoesNotExist:
            sink = None
        if network is not None:
            print('net exist')
            if sink is not None:
                i = 0    #compteur de capteur
                while i<len(request.data['sensors']):
                    if sink.sink_key == network.network_key:
                        try:
                            sensor_t = Capteur.objects.get(adresse_capteur=request.data['sensors'][i]['sensor_address'])
                        except Capteur.DoesNotExist:
                            sensor_t = None
                        if sensor_t is None:
                            sensor = Capteur(
                                    nom_capteur = request.data['sensors'][i]['sensor_name'],
                                    adresse_capteur = request.data['sensors'][i]['sensor_address'],
                                    description_capteur = request.data['sensors'][i]['sensor_description'],
                                    reseau_id = network.id
                                )
                            sensor.save()

                        data_app = Donnee_appli(
                            valeur_brute  = request.data['sensors'][i]['datas']['valeur'],
                            valeur_traite = request.data['sensors'][i]['datas']['valeur'],
                            type_data  = request.data['sensors'][i]['datas']['type'],
                            unity_data = request.data['sensors'][i]['datas']['unite'],
                            capteur_id = sensor_t.id if sensor_t is not None else sensor.id
                        )
                        data_app.save()
                    else:
                        pass
                    i += 1
            else:
                pass
        return Response({'done': True})
    elif request.data['operation'] == "addCtrlData":
        try:    
            network = Reseau.objects.get(network_key=request.data['network_key'])
        except Reseau.DoesNotExist:
            network = None
        try:
            sink    = Puits.objects.get(sink_key=request.data['sink_key'])
        except Puits.DoesNotExist:
            sink = None
        if network is not None:
            if sink is not None:
                i = 0    #compteur de capteur
                while i<len(request.data['sensors']):
                    if sink.sink_key == network.network_key:
                        try:
                            sensor_t = Capteur.objects.get(adresse_capteur=request.data['sensors'][i]['sensor_address'])
                        except Capteur.DoesNotExist:
                            sensor_t = None
                        if sensor_t is None:
                            sensor = Capteur(
                                    nom_capteur = request.data['sensors'][i]['sensor_name'],
                                    adresse_capteur = request.data['sensors'][i]['sensor_address'],
                                    description_capteur = request.data['sensors'][i]['sensor_description'],
                                    reseau_id = network.id
                                )
                            sensor.save()

                        data_ctrl = Donnee_ctrl(
                            lq  = request.data['sensors'][i]['datas']['lq'],
                            rssi = request.data['sensors'][i]['datas']['rssi'],
                            voisin  = request.data['sensors'][i]['datas']['voisin'],
                            capteur_id = sensor_t.id if sensor_t is not None else sensor.id
                        )
                        data_ctrl.save()
                        state_sensor = Etat_capteur(
                            energie  = request.data['sensors'][i]['etat']['energie'],
                            capteur_id = sensor_t.id if sensor_t is not None else sensor.id
                        )
                        state_sensor.save()
                    else:
                        pass
                    i += 1 #next sensor
                else:
                    pass
        return Response({'done': True})
    else:
        print("On ne se comprend pas!!!")



    {
        "operation": "addAppData",
        "network_key": "net0669222008241825",
        "sink_key": "net0669222008241825",
        "sensors": [{
            "sensor_name": "sensor-2",
            "sensor_address": "2.5",
            "sensor_description": "desc2.5",
            "datas": {
                "type": "température",
                "valeur": 15,
                "unite": "oC"
            }
        },
        {
            "sensor_name": "sensor-4",
            "sensor_address": "2.6",
            "sensor_description": "desc2.6",
            "datas": {
                "type": "température",
                "valeur": 15,
                "unite": "oC"
            }
        }]
    }

    {
    "operation": "addCtrlData",
        "network_key": "net0669222008241825",
        "sink_key": "net0669222008241825",
        "sensors": [{
            "sensor_name": "sensor-8",
            "sensor_address": "2.8",
            "sensor_description": "desc",
            "etat": {
                "energie": 30
            },
            "datas": {
                "voisin": ["4.1", "4.2"],
                "lq": 15,
                "rssi": 5
            }
        },
        {
            "sensor_name": "sensor-7",
            "sensor_address": "5.6",
            "sensor_description": "description5.6",
            "etat": {
                "energie": 100
            },
            "datas": {
                "voisin": ["1.5", "1.8"],
                "lq": 15,
                "rssi": 5
            }
        }]
    }
