from rest_framework import serializers

from .models import BreederResult

class BreederResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreederResult
        fields = '__all__'