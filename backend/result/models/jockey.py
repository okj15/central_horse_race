from basic_info.models.jockey import Jockey as BaseJockey
from django.db import models


class Jockey(models.Model):
    year = models.IntegerField()
    rank = models.IntegerField()
    first = models.IntegerField()
    second = models.IntegerField()
    third = models.IntegerField()
    unplaced = models.IntegerField()
    graded_runs = models.IntegerField()
    graded_wins = models.IntegerField()
    special_runs = models.IntegerField()
    special_wins = models.IntegerField()
    general_runs = models.IntegerField()
    general_wins = models.IntegerField()
    turf_runs = models.IntegerField()
    turf_wins = models.IntegerField()
    dirt_runs = models.IntegerField()
    dirt_wins = models.IntegerField()
    win_rate = models.FloatField()
    quinella_rate = models.FloatField()
    show_rate = models.FloatField()
    earnings = models.FloatField()
    jockey = models.ForeignKey(BaseJockey, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '騎手成績'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['year', 'jockey'],
                name="jockey_unique"
            )
        ]

    def __str__(self):
        return self.jockey.name
