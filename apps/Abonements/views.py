from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.Abonements.models import Abonement
from apps.Abonements.serializers import (
    AbonementValidatorSerializer, AbonementSerializer)


class AbonementViewAPI(ListCreateAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer

    def create(self, request, *args, **kwargs):
        serializer = AbonementValidatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director = Abonement.objects.create(**serializer.validated_data)

        return Response(data=AbonementSerializer(director).data,  status=status.HTTP_201_CREATED)


class AbonementDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Abonement.objects.all()
    serializer_class = AbonementSerializer
    lookup_field = 'id'