from rest_framework import serializers

from jockey.models import Master as JockeyMaster
from owner.models import Master as OwnerMaster
from trainer.models import Master as TrainerMaster
from ..models import Master as RacingHorseMaster, RacingHorseResult


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerMaster
        fields = '__all__'


class JockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = JockeyMaster
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerMaster
        fields = '__all__'


class HorseResultSerializer(serializers.ModelSerializer):
    jockey = JockeySerializer()
    trainer = TrainerSerializer()

    class Meta:
        model = RacingHorseResult
        fields = ['id', 'race_id', 'bracket', 'get_gender_display', 'jockey_weight', 'horse_number', 'race_time',
                  'popularity', 'odds', 'rank', 'get_training_center_display', 'jockey', 'trainer']


class RacingHorseSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    results = serializers.SerializerMethodField()

    class Meta:
        model = RacingHorseMaster
        fields = ['id', 'name', 'owner', 'breeder', 'results']

    def get_results(self, obj):
        try:
            queryset = RacingHorseResult.objects.filter(horse__id=obj.id)
            return HorseResultSerializer(queryset, many=True).data
        except Exception:
            return []
