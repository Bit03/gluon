from rest_framework import generics
from dapps.serializers import DAppSerializers, GitHub
from dapps.models import DApp


class DAppListAPIView(generics.ListAPIView):

    serializer_class = DAppSerializers
    queryset = DApp.objects.all()
    filter_fields = ('status', 'ico_status', )



