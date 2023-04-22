import http

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderWebhookViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_name'

    def update(self, request, order_name=None, *args, **kwargs):
        try:
            OrderSerializer(data=self.queryset.filter(order_name=order_name).update(**request.data))
            return Response(status=http.HTTPStatus.OK)
        except Exception as e:
            return Response(status=http.HTTPStatus.BAD_REQUEST, data="Что-то пошло не так")
