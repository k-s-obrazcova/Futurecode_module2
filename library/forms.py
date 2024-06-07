import re

from django.core.exceptions import ValidationError

from .models import Publishing_house
from django import forms

class Publishing_houseForm(forms.ModelForm):
    class Meta:
        model = Publishing_house
        fields = (
            'title',
            'agent_name',
            'agent_secondname',
            'agent_surname',
            'telephone',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form_control'}
            ),
            'agent_name': forms.TextInput(
                attrs={'class': 'form_control'}
            ),
            'agent_secondname': forms.TextInput(
                attrs={'class': 'form_control'}
            ),
            'agent_surname': forms.TextInput(
                attrs={'class': 'form_control'}
            ),
            'telephone': forms.TextInput(
                attrs={'class': 'form_control'}
            ),
        }
    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', telephone):
            return telephone
        raise ValidationError('Телефон не соответствует шаблону +7(ХХХ)ХХХ-ХХ-ХХ')