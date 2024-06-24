import re
from django.core.exceptions import ValidationError
from django import forms
from .models import *
class ProductFilterForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        min_length=2,
        strip=True,
        label='Название товара',
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )

    )

    max_price = forms.DecimalField(
        label='Максимальная цена товара',
        required=False,
        min_value=0,
        max_digits=10,
        decimal_places=2,
        step_size=0.01,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )
    )

    min_price = forms.DecimalField(
        label='Минимальная цена товара',
        required=False,
        min_value=0,
        max_digits=10,
        decimal_places=2,
        step_size=0.01,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )
    )
