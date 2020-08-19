from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
        instance.proprietaire.save()

