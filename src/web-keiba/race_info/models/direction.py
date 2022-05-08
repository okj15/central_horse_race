from django.db import models

class Direction(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = '回り'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name