from django.db import models


class Breeder(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()

    class Meta:
        verbose_name = '生産者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
