from django.contrib import admin
from django.urls import path, include
from . import views


# On import les vues de Django, avec un nom spécifique
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home1),
    path('home', views.home, name='home'),
    path('accueil', views.home, name='accueil'),
    path('nouveau_reseau', views.nouveau_reseau, name='nouveau_reseau'),
    path('mes_reseau', views.liste_reseau, name='reseau_list'),
    path('mon_profil', views.mon_profil),
    path('contact', views.contact, name='contact'),
    path('conditions', views.conditions, name='conditions'),
    path('a_propos', views.a_propos, name='a_propos'),
    path('aide', views.aide, name='aide'),
    path('abonnement', views.abonnement, name='abonnement'),
] 