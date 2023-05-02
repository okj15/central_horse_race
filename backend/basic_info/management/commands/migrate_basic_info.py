from django.core.management.base import BaseCommand

from result.models import Race as OldRace
from race.models import Race as NewRace
from racing_horse.models import RacingHorseResult, Master as Horse

from jockey.models import Master as Jockey
from trainer.models import Master as Trainer


class Command(BaseCommand):

    def handle(self, *args, **options):

        for old_data in OldRace.objects.all().order_by('id'):

            if old_data.id < 76657:
                continue

            race_id = NewRace.objects.get(race_id=old_data.race_id)
            horse = Horse.objects.get(id=old_data.horse_id)

            try:
                jockey = Jockey.objects.get(id=old_data.jockey_id)
            except:
                jockey = None
            try:
                trainer = Trainer.objects.get(id=old_data.trainer_id)
            except:
                trainer = None

            RacingHorseResult.objects.create(
                rank=old_data.rank,
                bracket=old_data.bracket,
                horse_number=old_data.horse_number,
                gender=old_data.gender,
                age=old_data.age,
                jockey_weight=old_data.jockey_weight,
                race_time=old_data.race_time,
                popularity=old_data.popularity,
                odds=old_data.odds,
                three_halon=old_data.three_halon,
                first_corner_rank=old_data.first_corner_rank,
                second_corner_rank=old_data.second_corner_rank,
                third_corner_rank=old_data.third_corner_rank,
                fourth_corner_rank=old_data.fourth_corner_rank,
                training_center=old_data.training_center,
                horse_weight=old_data.horse_weight,
                horse_weight_change=old_data.horse_weight_change,
                race_id=race_id,
                horse=horse,
                jockey=jockey,
                trainer=trainer
            )



