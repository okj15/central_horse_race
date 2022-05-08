from django.db import models


class Stallion(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()

    class Meta:
        verbose_name = '種牡馬'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name