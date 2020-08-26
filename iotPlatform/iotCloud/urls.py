from django.contrib import admin
from django.urls import path, include
from iotCloud import views


# On import les vues de Django, avec un nom spécifique
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home1),
    path('home', views.home, name='home'),
    path('accueil', views.home, name='accueil'),
    path('nouveau_reseau', views.nouveau_reseau, name='nouveau_reseau'),
    path('mes_reseau', views.liste_reseau, name='reseau_list'),
    path('mon_profil', views.mon_profil, name='mon_profil'),
    path('abonnement', views.abonnement, name='abonnement'),

    path('contact', views.contact, name='contact'),
    path('conditions', views.conditions, name='conditions'),
    path('a_propos', views.a_propos, name='a_propos'),
    path('aide', views.aide, name='aide'),

    path('network/<int:reseau_id>', views.sensor_list, name='sensor_list'),
    path('network/list-data/sensor-<int:sensor_id>', views.select_sensor_data, name='select_sensor_data'),
    path('network/<int:id>', views.sensors_by_network, name='sensors_by_network'),
] 
