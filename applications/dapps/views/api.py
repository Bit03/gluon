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

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        if self.request.user.is_superuser:
            return AdminDAppSerializers
        else:
            assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
            )

            return self.serializer_class

    # def get_serializer(self, *args, **kwargs):
    #     """
    #     Return the serializer instance that should be used for validating and
    #     deserializing input, and for serializing output.
    #     """
    #     if self.request.user.is_superuser:
    #         serializer_class = AdminDAppSerializers
    #     else:
    #         serializer_class = self.get_serializer_class()
    #     kwargs['context'] = self.get_serializer_context()
    #     return serializer_class(*args, **kwargs)


class DAppPlatformAPIView(generics.ListAPIView):
    serializer_class = DAppPlatformSerializers
    queryset = DApp.objects.exclude(platform="").values('platform').distinct()
