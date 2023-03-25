from rest_framework import routers
from licitacions import api

router = routers.DefaultRouter()

router.register('api/licitacions_publiques', api.LicitacioPublicaViewSet, 'licitacions_publiques')
router.register('api/licitacions_privades', api.LicitacioPrivadaViewSet, 'licitacions_privades')
router.register('api/localitzacions', api.LocalitzacioViewSet, 'localitzacions')
router.register('api/ambit', api.AmbitViewSet, 'ambits')
router.register('api/departament', api.DepartamentViewSet, 'departaments')
router.register('api/organ', api.OrganViewSet, 'organs')
router.register('api/tipus_contracte', api.TipusContracteViewSet, 'tipus_contracte')
router.register('api/location_barcelona', api.BarcelonaViewSet, 'barna')


urlpatterns = router.urls