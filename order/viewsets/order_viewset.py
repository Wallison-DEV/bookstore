
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

