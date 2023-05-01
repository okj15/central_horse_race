from django.db import models


class Master(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()

    class Meta:
        verbose_name = '調教師マスタ'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
