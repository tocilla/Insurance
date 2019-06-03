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


class RiskSerializer(serializers.ModelSerializer):
    # risk_type = RiskTypeSerializer(many=False, read_only=True)
    # risk_type_id = serializers.IntegerField(write_only=True)
    risk_inputs = RiskInputSerializer(many=True,required=True)

    class Meta:
        model = Risk
        fields = ('id','name','risk_type',
                  'risk_inputs', 'created_at',)
        filter_backends = (filters.OrderingFilter,)
        ordering_fields = ('name','risk_type','created_at')

    @transaction.atomic
    def create(self, validated_data):
        """
        Create and return a new `Risk` instance, given the validated data.
        """
        risk_inputs_data = validated_data.pop('risk_inputs')
        risk = Risk.objects.create(**validated_data)

        for risk_input_data in risk_inputs_data:
            risk_field = risk_input_data["risk_field"] #RiskField.objects.get(pk=risk_input_data["risk_field_id"])
            if risk_field.required is True and not risk_input_data["value"]:
                error = {'risk_inputs':['Empty value is not allowed on required inputs']}
                raise serializers.ValidationError(error)

            risk.risk_inputs.create(**risk_input_data)
        return risk
