# # Create your views here.
from rest_framework import viewsets, generics
# from rest_framework.viewsets import GenericViewSet
from .models import Risk
from .serializers import RiskSerializer


class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
