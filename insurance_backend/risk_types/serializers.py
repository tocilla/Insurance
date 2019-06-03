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


class RiskTypeSerializer(serializers.ModelSerializer):
    risk_fields = RiskFieldSerializer(many=True, required=True)

    class Meta:
        model = RiskType
        fields = ('id', 'name', 'description',
                  'risk_fields', 'active', 'created_at',)
        filter_backends = (filters.OrderingFilter,)
        ordering_fields = ('name', 'created_at')

    @transaction.atomic
    def create(self, validated_data):
        """
        Create and return a new `RiskType` instance, given the validated data.
        """
        risk_fields_data = validated_data.pop('risk_fields')

        risk_type = RiskType.objects.create(**validated_data)
        for risk_field_data in risk_fields_data:
            field_options_data = risk_field_data.pop('field_options')
            risk_field = risk_type.risk_fields.create(**risk_field_data)

            for field_option_data in field_options_data:
                if risk_field_data['type'] is 'option':
                    risk_field.field_options.create(**field_option_data)

        return risk_type
