# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import RiskType
from .serializers import RiskTypeSerializer


class RiskTypeViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
