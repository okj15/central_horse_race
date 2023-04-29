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

    race_id = models.IntegerField()                                             # レースID
    race_date = models.DateField()                                              # 開催日
    venue = models.IntegerField(null=True, choices=VENUE)                       # 開催場所
    race_class = models.IntegerField()                                          # レースの格付け
    race_number = models.IntegerField()                                         # レース番号
    track_type = models.IntegerField(null=True, choices=TRACK_TYPE)             # 芝orダート
    distance = models.IntegerField()                                            # レースの距離
    track_condition = models.IntegerField(null=True, choices=TRACK_CONDITION)   # 馬場状態
    direction = models.IntegerField(null=True, choices=DIRECTION)               # 右回りor左回りor直線
    weather = models.IntegerField(null=True, choices=WEATHER)                   # 天気
    starters = models.IntegerField()                                            # 出走頭数
    rank = models.IntegerField(null=True)                                       # 着順
    bracket = models.IntegerField(null=True)                                    # 枠番
    horse_number = models.IntegerField(null=True)                               # 馬番
    horse = models.ForeignKey(Horse, on_delete=models.SET_NULL, null=True)      # 馬名
    gender = models.IntegerField(null=True, choices=GENDER)                     # 性別
    age = models.IntegerField()                                                 # 年齢
    jockey_weight = models.IntegerField(null=True)                              # 騎手の体重
    jockey = models.ForeignKey(Jockey, on_delete=models.SET_NULL, null=True)    # 騎手
    race_time = models.FloatField(null=True)                                    # タイム
    popularity = models.FloatField(null=True)                                   # 人気
    odds = models.FloatField(null=True)                                         # オッズ
    three_halon = models.FloatField(null=True)                                  # 3ハロン 時間
    first_corner_rank = models.FloatField(null=True)                            # 1コーナー順位
    second_corner_rank = models.FloatField(null=True)                           # 2コーナー順位
    third_corner_rank = models.FloatField(null=True)                            # 3コーナー順位
    fourth_corner_rank = models.FloatField(null=True)                           # 4コーナー順位
    training_center = models.IntegerField(null=True, choices=TRAINING_CENTER)   # 調教師の所属
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)  # 調教師
    horse_weight = models.IntegerField(null=True)                               # 馬体重
    horse_weight_change = models.IntegerField(null=True)                        # 馬体重の変化

    class Meta:
        verbose_name = 'レース成績'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['race_id', 'horse'],
                name="race_unique"
            )
        ]
