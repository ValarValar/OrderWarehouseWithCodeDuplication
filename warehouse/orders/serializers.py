from rest_framework import serializers

from .models import WarehouseOrder


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = 'order_name', 'status'
