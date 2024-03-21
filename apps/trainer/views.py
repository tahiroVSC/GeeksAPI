from apps.trainer.models import Trainer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.trainer.serializers import TrainerSerializer


class TrainerViewAPI(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    lookup_field = 'id'
