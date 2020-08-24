from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from accounts.models import Proprietaire
# 1 ################################################################################
"""
class Proprietaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    telephone_proprio = models.CharField(max_length = 15, verbose_name="Numéro de téléphone")
    
    def __str__(self):
        return " %s " % (self.user)

    @receiver(post_save, sender = User)
    def create_user_propietaire(sender, instance, created, **kwargs):
        if created:
            Proprietaire.objects.create(user = instance)

    @receiver(post_save, sender = User)
    def save_user_propietaire(sender, instance, **kwargs):
        instance.proprietaire.save()"""

# 2 ################################################################################

class Reseau(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete = models.CASCADE)
    nom_reseau = models.CharField(max_length = 30, unique=True)
    network_key = models.CharField(max_length = 20, unique=True)
    date_creation = models.DateTimeField(default = timezone.now)
    description_reseau = models.TextField(max_length = 500)

    def __str__(self):
        return "%s" % (self.nom_reseau)
        
    """ 
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('gestionIoT.views.details', arg=[str(self.id)])"""

class Puits(models.Model):
    reseau = models.ForeignKey(Reseau, on_delete = models.CASCADE)
    adresse = models.CharField(max_length=15, unique=True)
    sink_key = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return " %s du réseau %s" % (self.adresse, self.reseau)

# 3 ################################################################################

class Capteur(models.Model):
    reseau = models.ForeignKey(Reseau, on_delete = models.CASCADE)
    nom_capteur = models.CharField(max_length = 30, unique=True)
    adresse_capteur = models.CharField(max_length = 30,  unique=True)
    description_capteur = models.TextField(max_length = 150)

    def __str__(self):
        return "%s : %s" % (self.nom_capteur, self.adresse_capteur)

# 4 ################################################################################

class Etat_capteur(models.Model):
    capteur = models.ForeignKey(Capteur, on_delete = models.CASCADE)
    energie = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "%s : %s" % (self.capteur, str(self.energie))

# 5 ################################################################################

class Service(models.Model):
    nom = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    duree = models.IntegerField()
    cout = models.FloatField(unique=True)

    def __str__(self):
        return '%s' % (self.nom)

# 6 ################################################################################

class Souscription(models.Model):
    reseau = models.ForeignKey(Reseau, on_delete=models.CASCADE)
    proprietaire = models.ForeignKey(Proprietaire, on_delete = models.CASCADE)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    date_sous = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s, %s' % (self.proprietaire, self.service)

# 8 ################################################################################

class Donnee_ctrl(models.Model):
    capteur = models.ForeignKey(Capteur, on_delete = models.CASCADE)
    lq     = models.FloatField()
    rssi   = models.FloatField()
    voisin = models.TextField(max_length= 1000)
    date = models.DateTimeField(auto_now_add=True)
    heure = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % (str(self.taux_livraison))

# 9 ################################################################################

class Donnee_appli(models.Model):
    capteur = models.ForeignKey(Capteur, on_delete = models.CASCADE)
    valeur_brute  = models.IntegerField()
    valeur_traite = models.FloatField()
    type_data     = models.CharField(max_length=30)
    unity_data    = models.CharField(max_length=10)
    date          = models.DateField(auto_now_add=True)
    heure         = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s" % (str(self.valeur_traite))

#################################################################################
