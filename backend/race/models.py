from django.db import models


class Race(models.Model):
    DIRECTION = (
        (1, '右'),
        (2, '左'),
        (3, '直接'),
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

    race_id = models.IntegerField()  # レースID
    race_date = models.DateField()  # 開催日
    venue = models.IntegerField(null=True, choices=VENUE)  # 開催場所
    race_class = models.IntegerField()  # レースの格付け
    race_number = models.IntegerField()  # レース番号
    track_type = models.IntegerField(null=True, choices=TRACK_TYPE)  # 芝orダート
    distance = models.IntegerField()  # レースの距離
    track_condition = models.IntegerField(null=True, choices=TRACK_CONDITION)  # 馬場状態
    direction = models.IntegerField(null=True, choices=DIRECTION)  # 右回りor左回りor直線
    weather = models.IntegerField(null=True, choices=WEATHER)  # 天気
    starters = models.IntegerField()  # 出走頭数

    class Meta:
        verbose_name = 'レース情報'
        verbose_name_plural = verbose_name
