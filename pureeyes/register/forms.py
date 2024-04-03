from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['owner_name', 'animal_name', 'animal_age', 'animal_type', 'email', 'mobile_number', 'notes']
