from django.urls import path, include


from .views import *

urlpatterns = [
    path('api/v1/users_psg_list/', UserPSGApiList.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/users_psg_list/<int:pk>/', UserPSGApiUpdate.as_view()),
    path('api/v1/users_psg_list_delete/<int:pk>/', UserPSGApiDestroy.as_view()),
]