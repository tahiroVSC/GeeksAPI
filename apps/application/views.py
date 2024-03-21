from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from apps.application.serializers import ApplicationSerializers
from apps.application.models import Application


class ApplicationsAPIViews(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializers


# class ApplicatonDetailAPIVeiws(RetrieveUpdateDestroyAPIView):
#     queryset = Application.objects.all()
#     serializer_class = ApplicationSerializers
#     lookup_field = 'id'
