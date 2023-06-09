import os

import requests
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order
from .serializers import OrderSerializer

WAREHOUSE_URL = os.getenv("WAREHOUSE_URL")

@receiver(post_save, sender=Order)
def order_create_update_signal(sender, instance: Order, created, **kwargs):
    serialized_data = OrderSerializer(instance).data
    post_url = f'{WAREHOUSE_URL}/order_webhooks/order/'
    patch_url = f'{WAREHOUSE_URL}/order_webhooks/order/{instance.order_name}/'
    if created:
        requests.post(post_url, json=serialized_data)
    else:
        requests.patch(patch_url, json=serialized_data)


@receiver(post_delete, sender=Order)
def order_delete_signal(sender, instance: Order, **kwargs):
    delete_url = f'{WAREHOUSE_URL}/order_webhooks/order/{instance.order_name}/'
    requests.delete(delete_url)
