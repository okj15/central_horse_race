from rest_framework import serializers

from .models import OwnerResult

class OwnerResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerResult
        fields = '__all__'