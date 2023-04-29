from django.contrib import admin

from ..admin.direction import DirectionAdmin
from ..admin.gender import GenderAdmin
from ..admin.track_condition import TrackConditionAdmin
from ..admin.track_type import TrackTypeAdmin
from ..admin.training_center import TrainingCenterAdmin
from ..admin.venue import VenueAdmin
from ..admin.weather import WeatherAdmin
from ..models import Direction
from ..models import Gender
from ..models import TrackCondition
from ..models import TrackType
from ..models import TrainingCenter
from ..models import Venue
from ..models import Weather

admin.site.register(Venue, VenueAdmin)
admin.site.register(TrackType, TrackTypeAdmin)
admin.site.register(TrackCondition, TrackConditionAdmin)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(Weather, WeatherAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(TrainingCenter, TrainingCenterAdmin)
