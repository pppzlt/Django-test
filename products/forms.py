# from socket import fromshare
# from turtle import title
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title   =forms.CharField()
    decription=forms.CharField()
    price   = forms.DecimalField()
