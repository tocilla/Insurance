from django.db import transaction
from rest_framework import serializers, filters
from rest_framework.exceptions import ParseError
from .models import RiskType, RiskField, FieldOption


class RiskFieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOption
        fields = ('content',)


class RiskFieldSerializer(serializers.ModelSerializer):
    field_options = RiskFieldOptionSerializer(many=True, required=False)

    class Meta:
        model = RiskField
        fields = ('id', 'name', 'type', 'field_options', 'required',)


