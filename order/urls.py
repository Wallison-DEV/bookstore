from django.urls import include, path
from rest_framework import routers

from .viewsets import OrderViewSet

router = routers.SimpleRouter()
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
