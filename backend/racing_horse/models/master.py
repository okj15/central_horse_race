from django.db import models

from breeder.models import Master as Breeder
from breeding_horse.models import Master as BreedingHorse
from owner.models import Master as Owner


class Master(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    birthday = models.DateField()
    mother_id = models.TextField()
    father_father_id = models.TextField()
    father_mother_id = models.TextField()
    mother_mother_id = models.TextField()

    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    breeder = models.ForeignKey(Breeder, on_delete=models.SET_NULL, null=True)
    father = models.ForeignKey(BreedingHorse, on_delete=models.SET_NULL, null=True, related_name='sire')
    mother_father = models.ForeignKey(BreedingHorse, on_delete=models.SET_NULL, null=True, related_name='bms')

    class Meta:
        verbose_name = '競走馬マスタ'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
