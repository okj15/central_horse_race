from rest_framework import serializers

from ..models import Race
from basic_info.models import Jockey


class JockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jockey
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['id', 'race_id', 'horse', 'horse_number', 'age', 'get_gender_display']
