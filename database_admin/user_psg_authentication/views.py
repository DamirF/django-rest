from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .models import UserPSG
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .sersializers import UserPSGSerializer


class UserPSGApiList(generics.ListCreateAPIView):
    queryset = UserPSG.objects.all()
    serializer_class = UserPSGSerializer
    permission_classes = (IsAdminOrReadOnly, )


class UserPSGApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserPSG.objects.all()
    serializer_class = UserPSGSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class UserPSGApiDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPSG.objects.all()
    serializer_class = UserPSGSerializer
    permission_classes = (IsAdminOrReadOnly, )


