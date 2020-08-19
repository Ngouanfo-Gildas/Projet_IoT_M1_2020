from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Proprietaire
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm1(ModelForm):
    class Meta:
        model = User
        fields = ['username', 
            'first_name', 
            'last_name', 
            'email', 
            'password'
        ]
        labels = {'username':('Nom d\'utilisateur'), 
            'first_name':('Votre prénom'),  
            'last_name':('Votre nom de famille'),
            'mail':('Votre adresse mail'), 
            'password':('Mot de passe')
        }
        widgets ={'password': forms.PasswordInput}

class ProprietaireForm1(ModelForm):
    class Meta:
        model = Proprietaire
        fields = ['telephone_proprio']
        labels = {'telephone_proprio':('Numéro de téléphone')}
        
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

