from rest_framework import routers
from licitacions import api

router = routers.DefaultRouter()

router.register('api/licitacions_publiques', api.LicitacioPublicaPreviewViewSet, 'licitacions_publiques_preview')
router.register('api/licitacio_publica_details', api.LicitacioPublicaDetailsViewSet, 'licitacions_publiques_details')
router.register('api/licitacions_privades', api.LicitacioPrivadaPreviewViewSet, 'licitacions_privades_preview')
router.register('api/licitacio_privada_details', api.LicitacioPrivadaDetailsViewSet, 'licitacions_privades_details')
router.register('api/localitzacions', api.LocalitzacioViewSet, 'localitzacions')
router.register('api/ambit', api.AmbitViewSet, 'ambits')
router.register('api/departament', api.DepartamentViewSet, 'departaments')
router.register('api/organ', api.OrganViewSet, 'organs')
router.register('api/tipus_contracte', api.TipusContracteViewSet, 'tipus_contracte')
router.register('api/location_barcelona', api.BarcelonaViewSet, 'barna')


urlpatterns = router.urls