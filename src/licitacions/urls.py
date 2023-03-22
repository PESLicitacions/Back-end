from rest_framework import routers
from .api import LicitacioViewSet

router = routers.DefaultRouter()

router.register('api/licitacions', LicitacioViewSet, 'licitacions')

urlpatterns = router.urls