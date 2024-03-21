from rest_framework import serializers

from apps.trainer.models import Trainer


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class TrainerValidatorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    photo = serializers.ImageField(use_url=True, required=False)
    description = serializers.CharField(max_length=None)
