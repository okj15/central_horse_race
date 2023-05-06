from rest_framework import serializers

from .models import JockeyResult, Master

class JockeyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'

class JockeyResultSerializer(serializers.ModelSerializer):
    jockey = JockeyMasterSerializer(read_only=True)

    class Meta:
        model = JockeyResult
        fields = '__all__'