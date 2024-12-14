from rest_framework import viewsets, permissions

from spy_cats.models import SpyCats
from spy_cats.serializers import SpyCatsSerializer


class SpyCatsViewSet(viewsets.ModelViewSet):
    queryset = SpyCats.objects.all()
    serializer_class = SpyCatsSerializer
    permission_classes = [permissions.AllowAny]
