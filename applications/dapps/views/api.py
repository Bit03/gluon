from rest_framework import generics
from applications.dapps.serializers import DAppSerializers, DAppPlatformSerializers, AdminDAppSerializers
from applications.dapps.models import DApp


class DAppListAPIView(generics.ListAPIView):
    serializer_class = DAppSerializers
    queryset = DApp.objects.all()
    filter_fields = ('status', 'ico_status', 'platform')
    search_fields = ('name', )


class DAppDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DAppSerializers
    queryset = DApp.objects.all()
    lookup_field = 'slug'

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        if self.request.user.is_supperuser:
            serializer_class = AdminDAppSerializers()
        else:
            serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DAppPlatformAPIView(generics.ListAPIView):
    serializer_class = DAppPlatformSerializers
    queryset = DApp.objects.exclude(platform="").values('platform').distinct()
