from django.db import models

from jockey.models import Master as JockeyMaster
from race.models import Race
from trainer.models import Master as TrainerMaster
from .master import Master as HorseMaster


class RacingHorseResult(models.Model):
    GENDER = (
        (1, '牡'),
        (2, '牝'),
        (3, 'セ'),
    )

    TRAINING_CENTER = (
        (1, '美浦'),
        (2, '栗東')
    )

    rank = models.IntegerField(null=True)  # 着順
    bracket = models.IntegerField(null=True)  # 枠番
    horse_number = models.IntegerField(null=True)  # 馬番
    gender = models.IntegerField(null=True, choices=GENDER)  # 性別
    age = models.IntegerField()  # 年齢
    jockey_weight = models.IntegerField(null=True)  # 騎手の体重
    race_time = models.FloatField(null=True)  # タイム
    popularity = models.FloatField(null=True)  # 人気
    odds = models.FloatField(null=True)  # オッズ
    three_halon = models.FloatField(null=True)  # 3ハロン 時間
    first_corner_rank = models.FloatField(null=True)  # 1コーナー順位
    second_corner_rank = models.FloatField(null=True)  # 2コーナー順位
    third_corner_rank = models.FloatField(null=True)  # 3コーナー順位
    fourth_corner_rank = models.FloatField(null=True)  # 4コーナー順位
    training_center = models.IntegerField(null=True, choices=TRAINING_CENTER)  # 調教師の所属
    horse_weight = models.IntegerField(null=True)  # 馬体重
    horse_weight_change = models.IntegerField(null=True)  # 馬体重の変化

    race_id = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)  # レースID
    horse = models.ForeignKey(HorseMaster, on_delete=models.SET_NULL, null=True)  # 馬名
    jockey = models.ForeignKey(JockeyMaster, on_delete=models.SET_NULL, null=True)  # 騎手
    trainer = models.ForeignKey(TrainerMaster, on_delete=models.SET_NULL, null=True)  # 調教師

    class Meta:
        verbose_name = 'レース成績'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['race_id', 'horse'],
                name="race_result_unique"
            )
        ]
