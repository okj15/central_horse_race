
from django.core.management.base import BaseCommand

from ...models import Horse

from racing_horse.models import Master as RacingHorseMaster
from owner.models import Master as Owner
from breeder.models import Master as Breeder
from breeding_horse.models import Master as BreedingHorse



class Command(BaseCommand):

    def handle(self, *args, **options):
        # basic_infoのデータを新しいappに移行する
        for old_data in Horse.objects.all().order_by('id'):
            try:
                owner = Owner.objects.get(id=old_data.owner_id)
            except:
                owner = None
            try:
                breeder = Breeder.objects.get(id=old_data.breeder_id)
            except:
                breeder = None
            try:
                father = BreedingHorse.objects.get(id=old_data.father_id)
            except:
                print(old_data.father_id)
                father = None
            try:
                mother_father = BreedingHorse.objects.get(id=old_data.mother_father_id)
            except:
                print(old_data.mother_father_id)
                mother_father = None

            RacingHorseMaster.objects.create(
                id=old_data.id,
                name=old_data.name,
                birthday=old_data.birthday,
                mother_id=old_data.mother_id,
                father_father_id=old_data.father_father_id,
                father_mother_id=old_data.father_mother_id,
                mother_mother_id=old_data.mother_mother_id,
                owner=owner,
                breeder=breeder,
                father=father,
                mother_father=mother_father,
            )

