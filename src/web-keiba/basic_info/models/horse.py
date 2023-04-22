from django.db import models

from basic_info.models import Owner, Breeder, Stallion


class Horse(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    birthday = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    breeder = models.ForeignKey(Breeder, on_delete=models.SET_NULL, null=True)
    father = models.ForeignKey(Stallion, on_delete=models.SET_NULL, null=True, related_name='sire')
    mother_id = models.TextField()
    father_father_id = models.TextField()
    father_mother_id = models.TextField()
    mother_father = models.ForeignKey(Stallion, on_delete=models.SET_NULL, null=True, related_name='bms')
    mother_mother_id = models.TextField()

    class Meta:
        verbose_name = '競走馬'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
