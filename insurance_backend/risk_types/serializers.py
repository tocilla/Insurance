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

        if len(risk_fields_data) < 1:
            error = {'risk_fields': ['risk_fields should contain at least one risk_field']}
            raise serializers.ValidationError(error)

        risk_type = RiskType.objects.create(**validated_data)
        for risk_field_data in risk_fields_data:
            field_options_data = risk_field_data.pop('field_options')
            risk_field = risk_type.risk_fields.create(**risk_field_data)

            if len(field_options_data) < 2 and risk_field_data['type'] is 'option':
                error = {'field_options': [
                    'for option type it required to give at least two field_option']}
                raise serializers.ValidationError(error)

            if len(field_options_data) > 0 and risk_field_data['type'] is not 'option':
                error = {'field_options': [
                    'for ' + risk_field_data['type'] + ' type field can\'t have field options']}
                raise serializers.ValidationError(error)

            for field_option_data in field_options_data:
                if risk_field_data['type'] is 'option':
                    risk_field.field_options.create(**field_option_data)

        return risk_type
