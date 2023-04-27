from django.db import models

from basic_info.models.horse import Horse
from basic_info.models.jockey import Jockey
from basic_info.models.trainer import Trainer


class Race(models.Model):

    DIRECTION = (
        (1, '右'),
        (2, '左'),
        (3, '直接'),
    )

    GENDER = (
        (1, '牡'),
        (2, '牝'),
        (3, 'セ'),
    )

    TRACK_CONDITION = (
        (1, '良'),
        (2, '稍'),
        (3, '重'),
        (4, '不')
    )

    TRACK_TYPE = (
        (1, '芝'),
        (2, 'ダ'),
    )

    TRAINING_CENTER = (
        (1, '美浦'),
        (2, '栗東')
    )

    VENUE = (
        (1, '札幌'),
        (2, '函館'),
        (3, '福島'),
        (4, '新潟'),
        (5, '東京'),
        (6, '中山'),
        (7, '中京'),
        (8, '京都'),
        (9, '阪神'),
        (10, '小倉')
    )

    WEATHER = (
        (1, '晴'),
        (2, '曇'),
        (3, '小雨'),
        (4, '小雪'),
        (5, '雨'),
        (6, '雪'),
    )

    race_id = models.IntegerField()
    race_date = models.DateField()
    venue = models.IntegerField(null=True, choices=VENUE)
    race_class = models.IntegerField()
    race_number = models.IntegerField()
    track_type = models.IntegerField(null=True, choices=TRACK_TYPE)
    distance = models.IntegerField()
    track_condition = models.IntegerField(null=True, choices=TRACK_CONDITION)
    direction = models.IntegerField(null=True, choices=DIRECTION)
    weather = models.IntegerField(null=True, choices=WEATHER)
    starters = models.IntegerField()
    rank = models.IntegerField(null=True)
    bracket = models.IntegerField(null=True)
    horse_number = models.IntegerField(null=True)
    horse = models.ForeignKey(Horse, on_delete=models.SET_NULL, null=True)
    gender = models.IntegerField(null=True, choices=GENDER)
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
    training_center = models.IntegerField(null=True, choices=TRAINING_CENTER)
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
