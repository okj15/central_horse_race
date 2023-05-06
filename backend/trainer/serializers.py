from rest_framework import serializers

from .models import TrainerResult

class TrainerResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerResult
        fields = '__all__'