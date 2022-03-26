from django.contrib.auth.models import User, Group
from rest_framework import viewsets,serializers

from .models import Mechanic, ServicesTable, ShopInventory


class ShopInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ShopInventory
        fields=['name_of_part','price_of_part','car_make','car_model']

class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServicesTable
        fields=['service']

class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mechanic
        fields=['name_of_mechanic','service']
        depth=1