from django.db import models

# Create your models here.
from info_guides.models import Urgency, TypeOfCargo, DeliveryType
from user_psg_authentication.models import UserPSG


class Calc(models.Model):
    sending_point = models.CharField(max_length=150, verbose_name='Город отправки')
    arrival_point = models.CharField(max_length=150, verbose_name='Город прибытия')
    urgency = models.ForeignKey(Urgency, on_delete=models.CASCADE, verbose_name='Срочность доставки')
    type_of_cargo = models.ForeignKey(TypeOfCargo, on_delete=models.CASCADE, verbose_name='Тип груза')
    weight = models.FloatField(verbose_name='Вес')
    volume = models.FloatField(verbose_name='Объем')
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE, verbose_name='Тип доставки')
    declared_value_rate = models.IntegerField(verbose_name='Объявленная стоимость груза')
    insurance_rate = models.IntegerField(verbose_name='Страховая стоимость груза')

    is_test = models.BooleanField(default=False, verbose_name='Выключить тестовую версию')

    class Meta:
        db_table = 'table_004_calc_parameters'
