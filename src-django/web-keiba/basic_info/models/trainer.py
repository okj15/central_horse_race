from django.db import models


class Trainer(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()

    class Meta:
        verbose_name = '調教師'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
