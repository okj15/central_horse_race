from basic_info.models.horse import Horse
from basic_info.models.jockey import Jockey
from basic_info.models.trainer import Trainer
from django.db import models
from race_info.models import Venue, TrackType, TrackCondition, Direction, Weather, Gender, TrainingCenter


class Race(models.Model):
    race_id = models.IntegerField()
    race_date = models.DateField()
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    race_class = models.IntegerField()
    race_number = models.IntegerField()
    track_type = models.ForeignKey(TrackType, on_delete=models.SET_NULL, null=True)
    distance = models.IntegerField()
    track_condition = models.ForeignKey(TrackCondition, on_delete=models.SET_NULL, null=True)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)
    weather = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True)
    starters = models.IntegerField()
    rank = models.IntegerField(null=True)
    bracket = models.IntegerField(null=True)
    horse_number = models.IntegerField(null=True)
    horse = models.ForeignKey(Horse, on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField()
    jockey_weight = models.IntegerField(null=True)
    jockey = models.ForeignKey(Jockey, on_delete=models.SET_NULL, null=True)
    race_time = models.FloatField(null=True)
    popularity = models.FloatField(null=True)
    odds = models.FloatField(null=True)
    three_halon = models.FloatField(null=True)
    first_corner_rank = models.FloatField(null=True)
    second_corner_rank = models.FloatField(null=True)
    third_corner_rank = models.FloatField(null=True)
    fourth_corner_rank = models.FloatField(null=True)
    training_center = models.ForeignKey(TrainingCenter, on_delete=models.SET_NULL, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    horse_weight = models.IntegerField(null=True)
    horse_weight_change = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'レース成績'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['race_id', 'horse'],
                name="race_unique"
            )
        ]
