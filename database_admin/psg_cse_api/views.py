import json

from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsCalcUser
from .psg_cse_api_tools import calc_func
from .models import Calc, Urgency, TypeOfCargo, DeliveryType
from .psg_cse_api_tools.cse_to_db import send_calc_request
from .psg_cse_api_tools.pretty_response import transform_respone
from .serializers import CalcSerializer


class CalcCreateAPI(generics.CreateAPIView):
    queryset = Calc.objects.all()
    serializer_class = CalcSerializer
    permission_classes = (IsAuthenticated, IsCalcUser, )
    #authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        try:
            new_calc = Calc.objects.create(
                sending_point=request.data['sending_point'],
                arrival_point=request.data['arrival_point'],
                urgency=Urgency.objects.get(pk=int(request.data['urgency'])),
                type_of_cargo=TypeOfCargo.objects.get(pk=int(request.data['type_of_cargo'])),
                volume=request.data['volume'],
                weight=request.data['weight'],
                delivery_type=DeliveryType.objects.get(pk=int(request.data['delivery_type'])),
                declared_value_rate=request.data['declared_value_rate'],
                insurance_rate=request.data['insurance_rate'],
                is_test=bool(request.POST.get('is_test', False))
            )

            send_calc_request(sending_user=request.user.id,
                              sending_city=new_calc.sending_point,
                              arrival_city=new_calc.arrival_point,
                              volume=new_calc.volume,
                              weight=new_calc.weight,
                              is_test=new_calc.is_test,
                              declared_value_rate=new_calc.declared_value_rate
                              )
            return Response(json.loads(json.dumps(transform_respone(calc_func.ready_answer_calc_dict),
                                                  default=str,
                                                  ensure_ascii=False,
                                                  indent=2)))
        except Exception as _ex:
            print('[INFO]Error: ', _ex)
            return Response('{"Error": ""}')
