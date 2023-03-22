from .models import Licitacio
from rest_framework import viewsets, permissions
from .serializers import LicitacioSerializer

class LicitacioViewSet(viewsets.ModelViewSet):
    queryset = Licitacio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LicitacioSerializer