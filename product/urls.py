from django.urls import include, path
from rest_framework import routers

from .viewsets import ProductViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
