from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'owner_name', 'animal_name', 'animal_age', 'animal_type', 'email', 'mobile_number', 'notes']
