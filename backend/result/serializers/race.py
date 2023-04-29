from rest_framework import serializers

from basic_info.models import Jockey
from ..models import Race


class JockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jockey
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['id', 'race_id', 'horse', 'bracket', 'horse_number', 'age', 'get_gender_display', 'jockey_weight',
                  'race_time', 'popularity', 'odds']
