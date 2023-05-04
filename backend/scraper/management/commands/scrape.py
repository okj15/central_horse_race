from django.core.management import BaseCommand

from ...scrapers.breeder_scraper import BreederResultScraper
from ...scrapers.jockey_scraper import JockeyResultScraper
from ...scrapers.owner_scraper import OwnerResultScraper
from ...scrapers.trainer_scraper import TrainerResultScraper


# from ...scrapers.breeding_horse_scraper import BreedingHorseResultScraper
# from ...scrapers.racing_horse_scraper import RacingHorseResultScraper


class Command(BaseCommand):
    app_names = {
        'breeder': BreederResultScraper,
        'jockey': JockeyResultScraper,
        'owner': OwnerResultScraper,
        'trainer': TrainerResultScraper,
        # 'breeding_horse': 'BreedingHorseResultScraper',
        # 'racing_horse': 'RacingHorseResultScraper',
    }

    def add_arguments(self, parser):
        parser.add_argument('--app')
        parser.add_argument('--target')

    def handle(self, *args, **options):
        app_cls = self.app_names.get(options['app'], None)
        target_id = options['target']
        if not app_cls:
            return

        cls = app_cls(app_name=options["app"], target_id=target_id)

        soup = cls.scrape_html()
        res = cls.parse_soup(soup)
        # cls.save_db(res)
        print(res)
