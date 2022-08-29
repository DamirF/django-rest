from rest_framework import serializers

from info_guides.models import Urgency, TypeOfCargo, DeliveryType
from .models import Calc


def required(value):
    if value is None:
        raise serializers.ValidationError('This field is required')


class CalcSerializer(serializers.ModelSerializer):
    sending_point = serializers.CharField(max_length=150, validators=[required])
    arrival_point = serializers.CharField(max_length=150, validators=[required])
    # urgency = serializers.ForeignKey(Urgency, on_delete=serializers.CASCADE)
    # type_of_cargo = serializers.ForeignKey(TypeOfCargo, on_delete=serializers.CASCADE)
    weight = serializers.FloatField(validators=[required])
    volume = serializers.FloatField(validators=[required])
    # delivery_type = serializers.ForeignKey(DeliveryType, on_delete=serializers.CASCADE)
    declared_value_rate = serializers.IntegerField(validators=[required])
    insurance_rate = serializers.IntegerField(validators=[required])

    is_test = serializers.BooleanField(default=False)
    class Meta:
        model = Calc
        fields = ('sending_point',
                  'arrival_point',
                  'weight',
                  'volume',
                  'declared_value_rate',
                  'insurance_rate',
                  'is_test', )
