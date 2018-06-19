from rest_framework import generics
from applications.dapps.serializers import DAppSerializers, DAppPlatformSerializers
from applications.dapps.models import DApp


class DAppListAPIView(generics.ListAPIView):
    serializer_class = DAppSerializers
    queryset = DApp.objects.all()
    filter_fields = ('status', 'ico_status', 'platform')


class DAppPlatformAPIView(generics.ListAPIView):
    serializer_class = DAppPlatformSerializers
    queryset = DApp.objects.values('platform').distinct()
