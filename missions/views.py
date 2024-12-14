from rest_framework import viewsets, permissions, mixins

from missions.models import Missions, Targets
from missions.serializers import MissionsSerializer, TargetsSerializer


class MissionsViewSet(viewsets.ModelViewSet):
    queryset = Missions.objects.all().prefetch_related('targets')
    serializer_class = MissionsSerializer
    permission_classes = [permissions.AllowAny]


class TargetsUpdateOnlyViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Targets.objects.all()
    serializer_class = TargetsSerializer
    permission_classes = [permissions.AllowAny]
