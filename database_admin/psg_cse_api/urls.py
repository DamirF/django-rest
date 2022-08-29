from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/calc/', CalcCreateAPI.as_view()),
]