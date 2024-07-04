import re
from django.core.exceptions import ValidationError
from django import forms
from .models import *

class ProductFilterForm(forms.Form):
    name = forms.CharField(
        label='Название товара',
        required=False,
        min_length=2,
        max_length=150,
        strip=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    min_price = forms.DecimalField(
        label='Минимальная цена',
        required=False,
        min_value=0,
        max_digits=10,
        decimal_places=2,
        step_size=0.01,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )
    )
    max_price = forms.DecimalField(
        label='Максимальная цена',
        required=False,
        min_value=1,
        max_digits=10,
        decimal_places=2,
        step_size=0.01,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )
    )
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = (
            'name',
            'agent_lastname',
            'agent_name',
            'agent_surname',
            'agent_telephone',
            'address',
            'is_exists'
        )