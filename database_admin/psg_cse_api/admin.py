from django.contrib import admin
from .models import Calc, Urgency, TypeOfCargo, DeliveryType

# Register your models here.


class CalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'sending_point', 'arrival_point', 'volume', 'weight', 'is_test', )
    readonly_fields = list_display


admin.site.register(Calc, CalcAdmin)


