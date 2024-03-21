from rest_framework import serializers
from apps.About.models import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class AboutUsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class AboutUsValidatorSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=None)
