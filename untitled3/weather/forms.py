import requests
from django import forms
from weather.models import Cities
class CityForm(forms.ModelForm):
    class Meta:
        model=Cities
        fields=('name',)