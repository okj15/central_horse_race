from rest_framework import serializers

from basic_info.models import Jockey, Owner, Trainer, Horse
from ..models import Race


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class JockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jockey
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class HorseResultSerializer(serializers.ModelSerializer):
    jockey = JockeySerializer()
    trainer = TrainerSerializer()

    class Meta:
        model = Race
        fields = ['id', 'race_id', 'bracket', 'get_gender_display', 'jockey_weight', 'horse_number', 'race_time',
                  'popularity', 'odds', 'rank', 'get_training_center_display', 'jockey', 'trainer']


class HorseSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    results = serializers.SerializerMethodField()

    class Meta:
        model = Horse
        fields = ['id', 'name', 'owner', 'breeder', 'results']

    def get_results(self, obj):
        try:
            queryset = Race.objects.filter(horse__id=obj.id)
            return HorseResultSerializer(queryset, many=True).data
        except Exception:
            return []
