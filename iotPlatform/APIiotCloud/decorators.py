import json 

def add_data(donnee_appli):
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
    
        print("l\'indice est :", indice)
        print("l\'operation est :", operation)
        print("l\'id du network est :", network_id)
        print("l\'id du puits est :", sink_id)
        print("l\'id du capteur est :", id_s)
        print("l\'adresse du capteur est :", addr_s)
        print("la description est :", desc_s)
        print("le type de donnee est :", data_type)
        print("la valeur de la donne est :", data_valeur)
        print("l\'unite de la donne est :", data_unit)
        print("\n\n")
        indice = indice + 1

def add_ctrl(donnee_ctrl):
    data = json.loads(donnee_ctrl)
    operation = data['operation']
    network_id = data['networkID']
    sink_id = data['sinkID']
    indice = 0
    while indice<len(data['sensors']):
        sensor=data['sensors']
        id_s       = sensor[indice]['id']
        addr_s     = sensor[indice]['address']
        desc_s     = sensor[indice]['description']
        etat_s     = sensor[indice]['etat']['energie']
        data_voisin= sensor[indice]['datas']['voisin']
        data_lq    = sensor[indice]['datas']['lq']
        data_rssi  = sensor[indice]['datas']['rssi']
    
        print("l\'indice est :", indice)
        print("l\'operation est :", operation)
        print("l\'id du network est :", network_id)
        print("l\'id du puits est :", sink_id)
        print("l\'id du capteur est :", id_s)
        print("l\'adresse du capteur est :", addr_s)
        print("la description est :", desc_s)
        print("l\'energie du capteur est :", etat_s)
        print("adresses des voisins :", data_voisin)
        print("la data_lq est :", data_lq)
        print("le rssi de la donne est :", data_rssi)
        print("\n\n")
        indice = indice + 1

    
    
data_appli = '{\
    "operation": "addAppData",\
    "networkID": "122",\
    "sinkID": 22,\
    "sensors": [{\
        "id": 5,\
        "address": "55",\
        "description": "desc",\
        "datas": {\
            "type": "température",\
            "valeur": 15,\
            "unite": "oC"\
        }\
    },\
    {\
        "id": 6,\
        "address": "56",\
        "description": "desc2",\
        "datas": {\
            "type": "humidite",\
            "valeur": 16,\
            "unite": "oK"\
        }\
    }]\
}'

data_ctrl='{\
    "operation": "addCtrlData",\
    "networkID": "122",\
    "sinkID": 22,\
    "sensors": [{\
        "id": 5,\
        "address": "55",\
        "description": "desc",\
        "etat": {\
            "energie": 30\
        },\
        "datas": {\
            "voisin": ["192.168.1.1", "192.168.1.2"],\
            "lq": 15,\
            "rssi": 5\
        }\
    }]\
}'

add_data(data_appli)
add_ctrl(data_ctrl)