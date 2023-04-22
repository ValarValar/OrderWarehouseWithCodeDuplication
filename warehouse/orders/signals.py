import os

import requests
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import WarehouseOrder
from .serializers import OrderSerializer

STORE_URL = os.getenv("STORE_URL")


@receiver(post_save, sender=WarehouseOrder)
def order_create_update_signal(sender, instance: WarehouseOrder, created, **kwargs):
    serialized_data = OrderSerializer(instance).data
    post_url = f'{STORE_URL}/order_webhooks/order/'
    patch_url = f'{STORE_URL}/order_webhooks/order/{instance.order_name}/'
    if created:
        requests.post(post_url, json=serialized_data)
    else:
        requests.patch(patch_url, json=serialized_data)


@receiver(post_delete, sender=WarehouseOrder)
def order_delete_signal(sender, instance: WarehouseOrder, **kwargs):
    delete_url = f'{STORE_URL}/order_webhooks/order/{instance.order_name}/'
    requests.delete(delete_url)
