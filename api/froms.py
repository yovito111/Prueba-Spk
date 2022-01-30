from django import forms
from django.db import models
from .models import Customer


class FormCustomer(forms.Form):
    """Formulario de Reistro de un cliente
    variables = 
    Nombre :
    Comment:
    """
    name = forms.CharField(label='Nombre',max_length=50, required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'row':5, 'cols':20 }))

class FormSaleOrder(forms.Form):
    comment= forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={'row':5, 'cols':20 }))
    date = forms.DateTimeField()
    total = forms.IntegerField()
    customer_id = forms.IntegerField()