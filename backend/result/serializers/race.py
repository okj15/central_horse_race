from rest_framework import serializers

from basic_info.models import Jockey, Owner, Trainer, Horse
from ..models import Race


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class HorseSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = Horse
        fields = ['id', 'name', 'owner', 'breeder']


class JockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jockey
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class RaceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['id', 'race_id', 'race_date', 'get_venue_display', 'race_class', 'race_number',
                  'get_track_type_display', 'get_track_condition_display',
                  'get_direction_display', 'distance', 'get_weather_display']


class RaceResultSerializer(serializers.ModelSerializer):
    horse = HorseSerializer()
    jockey = JockeySerializer()
    trainer = TrainerSerializer()

    class Meta:
        model = Race
        fields = ['id', 'race_id', 'bracket', 'horse', 'age', 'get_gender_display', 'jockey_weight',
                  'horse_number', 'race_time', 'popularity', 'odds', 'rank', 'get_training_center_display', 'jockey',
                  'trainer']
