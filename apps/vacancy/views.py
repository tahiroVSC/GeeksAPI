from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.vacancy.serializers import VacancySerializers
from apps.vacancy.models import Vacancy


class VacansyAPIViews(ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializers


class VacansyDetailAPIVeiws(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializers
    lookup_field = 'id'
