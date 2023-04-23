from django.db import models

from basic_info.models.stallion import Stallion


class Bms(models.Model):
    year = models.IntegerField()
    rank = models.IntegerField()
    foals = models.IntegerField()
    winners = models.IntegerField()
    runs = models.IntegerField()
    wins = models.IntegerField()
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
    ei = models.FloatField()
    earnings = models.FloatField()
    turf_average_distance = models.FloatField(null=True)
    dirt_average_distance = models.FloatField(null=True)
    bms = models.ForeignKey(Stallion, on_delete=models.CASCADE, related_name='bms_result')

    class Meta:
        verbose_name = '父母成績'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(
                fields=['year', 'bms'],
                name="bms_unique"
            )
        ]

    def __str__(self):
        return self.name