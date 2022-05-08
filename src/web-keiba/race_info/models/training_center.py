from django.db import models

class TrainingCenter(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'トレーニング・センター'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name