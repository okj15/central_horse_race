from rest_framework import serializers


from .models import Race

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['id', 'race_id', 'race_date', 'get_venue_display', 'race_class', 'race_number',
                  'get_track_type_display', 'get_track_condition_display',
                  'get_direction_display', 'distance', 'get_weather_display']