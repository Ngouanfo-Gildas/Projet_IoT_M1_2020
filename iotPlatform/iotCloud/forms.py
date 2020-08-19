from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Proprietaire, Reseau
from django_countries.widgets import CountrySelectWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

     
class ReseauForm(ModelForm):
    class Meta:
        model = Reseau
        fields = ['description_reseau', 'nom_reseau']
        labels = {'nom_reseau':('Nom du réseau'),'description_reseau':('Description du réseau')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
