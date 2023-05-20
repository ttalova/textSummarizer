from rest_framework import serializers
from .models import MethodModel


class MethodSerializer(serializers.Serializer):
    text = serializers.CharField()