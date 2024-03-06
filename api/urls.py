from django.urls import path
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

# A linha abaixo não é mais necessária, pois as URLs estão incluídas através do roteador
# urlpatterns = [
#     path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
#     path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
# ]
