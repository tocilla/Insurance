from django.db import transaction
from rest_framework import serializers, filters
from .models import Risk, RiskInput
from risk_types.models import RiskType, RiskField
from risk_types.serializers import RiskTypeSerializer, RiskFieldSerializer


class RiskInputSerializer(serializers.ModelSerializer):
    # risk_field = RiskFieldSerializer(many=False, read_only=True)
    # risk_field_id = serializers.IntegerField(write_only=True,required=True)

    class Meta:
        model = RiskInput
        fields = ('risk_field', 'value',)
