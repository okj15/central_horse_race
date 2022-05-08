from django.contrib import admin

from race_info.models import Venue
from race_info.models import TrackType
from race_info.models import TrackCondition
from race_info.models import Direction
from race_info.models import Weather
from race_info.models import Gender
from race_info.models import TrainingCenter

from race_info.admin.venue import VenueAdmin
from race_info.admin.track_type import TrackTypeAdmin
from race_info.admin.track_condition import TrackConditionAdmin
from race_info.admin.direction import DirectionAdmin
from race_info.admin.weather import WeatherAdmin
from race_info.admin.gender import GenderAdmin
from race_info.admin.training_center import TrainingCenterAdmin

admin.site.register(Venue, VenueAdmin)
admin.site.register(TrackType, TrackTypeAdmin)
admin.site.register(TrackCondition, TrackConditionAdmin)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(Weather, WeatherAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(TrainingCenter, TrainingCenterAdmin)