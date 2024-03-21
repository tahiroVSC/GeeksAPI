from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.About.models import AboutUs
from apps.About.serializers import (
    AboutUsValidatorSerializer, AboutUsSerializer, AboutUsDetailSerializer)


class AboutUsViewAPI(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def create(self, request, *args, **kwargs):
        serializer = AboutUsValidatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director = AboutUs.objects.create(**serializer.validated_data)
        return Response(data=AboutUsSerializer(director).data,  status=status.HTTP_201_CREATED)


class AboutUsDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsDetailSerializer
    lookup_field = 'id'
