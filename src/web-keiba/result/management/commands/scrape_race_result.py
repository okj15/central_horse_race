from django.core.management.base import BaseCommand
from django.conf import settings

from result.models import Jockey, Owner, Trainer, Breeder, Sire, Bms
from basic_info.models import Jockey as BaseJockey
from basic_info.models import Owner as BaseOwner
from basic_info.models import Trainer as BaseTrainer
from basic_info.models import Breeder as BaseBreeder
from basic_info.models import Stallion

from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm


class Command(BaseCommand):

    def insert_human(self, table, _id, soup):

        results = soup.find_all('tr')
        for result in results:
            if result.find('td') is None:
                continue
            if result.find('td').text.isdecimal():

                if result.find_all('td')[1].text == '':
                    continue

                win_rate = result.find_all('td')[16].text
                quinella_rate = result.find_all('td')[17].text
                show_rate = result.find_all('td')[18].text
                if win_rate == '.':
                    win_rate = win_rate.replace('.', '0.')
                if quinella_rate == '.':
                    quinella_rate = quinella_rate.replace('.', '0.')
                if show_rate == '.':
                    show_rate = show_rate.replace('.', '0.')

                earnings = result.find_all('td')[19].text.replace(',', '')

                if table == 'jockey':
                    jockey = BaseJockey.objects.filter(id=_id).first()
                    p = Jockey.objects.update_or_create(
                        year=result.find_all('td')[0].text,
                        rank=result.find_all('td')[1].text,
                        first=result.find_all('td')[2].text,
                        second=result.find_all('td')[3].text,
                        third=result.find_all('td')[4].text,
                        unplaced=result.find_all('td')[5].text.replace(',', ''),
                        graded_runs=result.find_all('td')[6].text.replace(',', ''),
                        graded_wins=result.find_all('td')[7].text.replace(',', ''),
                        special_runs=result.find_all('td')[8].text.replace(',', ''),
                        special_wins=result.find_all('td')[9].text.replace(',', ''),
                        general_runs=result.find_all('td')[10].text.replace(',', ''),
                        general_wins=result.find_all('td')[11].text.replace(',', ''),
                        turf_runs=result.find_all('td')[12].text.replace(',', ''),
                        turf_wins=result.find_all('td')[13].text.replace(',', ''),
                        dirt_runs=result.find_all('td')[14].text.replace(',', ''),
                        dirt_wins=result.find_all('td')[15].text.replace(',', ''),
                        win_rate=win_rate,
                        # quinella_rate=quinella_rate,
                        # show_rate=show_rate,
                        earnings=earnings,
                        jockey=jockey,
                        defaults={
                            'quinella_rate': quinella_rate,
                            'show_rate': show_rate
                        }
                    )
                elif table == 'trainer':
                    trainer = BaseTrainer.objects.filter(id=_id).first()
                    p = Trainer.objects.update_or_create(
                        year=result.find_all('td')[0].text,
                        rank=result.find_all('td')[1].text,
                        first=result.find_all('td')[2].text,
                        second=result.find_all('td')[3].text,
                        third=result.find_all('td')[4].text,
                        unplaced=result.find_all('td')[5].text.replace(',', ''),
                        graded_runs=result.find_all('td')[6].text.replace(',', ''),
                        graded_wins=result.find_all('td')[7].text.replace(',', ''),
                        special_runs=result.find_all('td')[8].text.replace(',', ''),
                        special_wins=result.find_all('td')[9].text.replace(',', ''),
                        general_runs=result.find_all('td')[10].text.replace(',', ''),
                        general_wins=result.find_all('td')[11].text.replace(',', ''),
                        turf_runs=result.find_all('td')[12].text.replace(',', ''),
                        turf_wins=result.find_all('td')[13].text.replace(',', ''),
                        dirt_runs=result.find_all('td')[14].text.replace(',', ''),
                        dirt_wins=result.find_all('td')[15].text.replace(',', ''),
                        win_rate=win_rate,
                        # quinella_rate=quinella_rate,
                        # show_rate=show_rate,
                        earnings=earnings,
                        trainer=trainer,
                        defaults={
                            'quinella_rate': quinella_rate,
                            'show_rate': show_rate
                        }
                    )
                elif table == 'owner':
                    owner = BaseOwner.objects.filter(id=_id).first()
                    p = Owner.objects.update_or_create(
                        year=result.find_all('td')[0].text,
                        rank=result.find_all('td')[1].text,
                        first=result.find_all('td')[2].text,
                        second=result.find_all('td')[3].text,
                        third=result.find_all('td')[4].text,
                        unplaced=result.find_all('td')[5].text.replace(',', ''),
                        graded_runs=result.find_all('td')[6].text.replace(',', ''),
                        graded_wins=result.find_all('td')[7].text.replace(',', ''),
                        special_runs=result.find_all('td')[8].text.replace(',', ''),
                        special_wins=result.find_all('td')[9].text.replace(',', ''),
                        general_runs=result.find_all('td')[10].text.replace(',', ''),
                        general_wins=result.find_all('td')[11].text.replace(',', ''),
                        turf_runs=result.find_all('td')[12].text.replace(',', ''),
                        turf_wins=result.find_all('td')[13].text.replace(',', ''),
                        dirt_runs=result.find_all('td')[14].text.replace(',', ''),
                        dirt_wins=result.find_all('td')[15].text.replace(',', ''),
                        win_rate=win_rate,
                        # quinella_rate=quinella_rate,
                        # show_rate=show_rate,
                        earnings=earnings,
                        owner=owner,
                        defaults={
                            'quinella_rate': quinella_rate,
                            'show_rate': show_rate
                        }
                    )
                elif table == 'breeder':
                    breeder = BaseBreeder.objects.filter(id=_id).first()
                    p = Breeder.objects.update_or_create(
                        year=result.find_all('td')[0].text,
                        rank=result.find_all('td')[1].text,
                        first=result.find_all('td')[2].text,
                        second=result.find_all('td')[3].text,
                        third=result.find_all('td')[4].text,
                        unplaced=result.find_all('td')[5].text.replace(',', ''),
                        graded_runs=result.find_all('td')[6].text.replace(',', ''),
                        graded_wins=result.find_all('td')[7].text.replace(',', ''),
                        special_runs=result.find_all('td')[8].text.replace(',', ''),
                        special_wins=result.find_all('td')[9].text.replace(',', ''),
                        general_runs=result.find_all('td')[10].text.replace(',', ''),
                        general_wins=result.find_all('td')[11].text.replace(',', ''),
                        turf_runs=result.find_all('td')[12].text.replace(',', ''),
                        turf_wins=result.find_all('td')[13].text.replace(',', ''),
                        dirt_runs=result.find_all('td')[14].text.replace(',', ''),
                        dirt_wins=result.find_all('td')[15].text.replace(',', ''),
                        win_rate=win_rate,
                        # quinella_rate=quinella_rate,
                        # show_rate=show_rate,
                        earnings=earnings,
                        breeder=breeder,
                        defaults={
                            'quinella_rate': quinella_rate,
                            'show_rate': show_rate
                        }
                    )


    def insert_breed(self, _id, soup):

        sire_result = soup.find( 'table', {'summary':'産駒成績'} )
        bms_result = soup.find( 'table', {'summary':'成績'} )

        for table, breed_results in zip(['sire', 'bms'], [sire_result, bms_result]):
            if breed_results is None or breed_results.find_all('tr') is None:
                continue

            results = breed_results.find_all('tr')
            for result in results:
                if result.find('td') is None:
                    continue
                if result.find('td').text.isdecimal():
                    # データがない場合次に飛ばす
                    if result.find_all('td')[2].text.replace(',', '') == '':
                        continue

                    win_rate = result.find_all('td')[16].text
                    ei = result.find_all('td')[17].text
                    if win_rate == '.':
                        win_rate = win_rate.replace('.', '0.')
                    if ei == '.':
                        ei = ei.replace('.', '0.')

                    sire = Stallion.objects.filter(id=_id).first()

                    if table == 'sire':
                        p = Sire.objects.update_or_create(
                            year=result.find_all('td')[0].text,
                            rank=result.find_all('td')[1].text,
                            foals=result.find_all('td')[2].text.replace(',', ''),
                            winners=result.find_all('td')[3].text.replace(',', ''),
                            runs=result.find_all('td')[4].text.replace(',', ''),
                            wins=result.find_all('td')[5].text.replace(',', ''),
                            graded_runs=result.find_all('td')[6].text.replace(',', ''),
                            graded_wins=result.find_all('td')[7].text.replace(',', ''),
                            special_runs=result.find_all('td')[8].text.replace(',', ''),
                            special_wins=result.find_all('td')[9].text.replace(',', ''),
                            general_runs=result.find_all('td')[10].text.replace(',', ''),
                            general_wins=result.find_all('td')[11].text.replace(',', ''),
                            turf_runs=result.find_all('td')[12].text.replace(',', ''),
                            turf_wins=result.find_all('td')[13].text.replace(',', ''),
                            dirt_runs=result.find_all('td')[14].text.replace(',', ''),
                            dirt_wins=result.find_all('td')[15].text.replace(',', ''),
                            win_rate=win_rate,
                            ei=ei,
                            # earnings=result.find_all('td')[18].text.replace(',', ''),
                            # turf_average_distance=result.find_all('td')[19].text.replace(',', ''),
                            # dirt_average_distance=result.find_all('td')[20].text.replace(',', ''),
                            sire=sire,
                            defaults={
                                'earnings': result.find_all('td')[18].text.replace(',', ''),
                                'turf_average_distance': result.find_all('td')[19].text.replace(',', ''),
                                'dirt_average_distance': result.find_all('td')[20].text.replace(',', '')
                            }
                        )
                    elif table == 'bms':
                        p = Bms.objects.update_or_create(
                            year=result.find_all('td')[0].text,
                            rank=result.find_all('td')[1].text,
                            foals=result.find_all('td')[2].text.replace(',', ''),
                            winners=result.find_all('td')[3].text.replace(',', ''),
                            runs=result.find_all('td')[4].text.replace(',', ''),
                            wins=result.find_all('td')[5].text.replace(',', ''),
                            graded_runs=result.find_all('td')[6].text.replace(',', ''),
                            graded_wins=result.find_all('td')[7].text.replace(',', ''),
                            special_runs=result.find_all('td')[8].text.replace(',', ''),
                            special_wins=result.find_all('td')[9].text.replace(',', ''),
                            general_runs=result.find_all('td')[10].text.replace(',', ''),
                            general_wins=result.find_all('td')[11].text.replace(',', ''),
                            turf_runs=result.find_all('td')[12].text.replace(',', ''),
                            turf_wins=result.find_all('td')[13].text.replace(',', ''),
                            dirt_runs=result.find_all('td')[14].text.replace(',', ''),
                            dirt_wins=result.find_all('td')[15].text.replace(',', ''),
                            win_rate=win_rate,
                            ei=ei,
                            # earnings=result.find_all('td')[18].text.replace(',', ''),
                            # turf_average_distance=result.find_all('td')[19].text.replace(',', ''),
                            # dirt_average_distance=result.find_all('td')[20].text.replace(',', ''),
                            bms=sire,
                            defaults={
                                'earnings': result.find_all('td')[18].text.replace(',', ''),
                                'turf_average_distance': result.find_all('td')[19].text.replace(',', ''),
                                'dirt_average_distance': result.find_all('td')[20].text.replace(',', '')
                            }
                        )


    def add_arguments(self, parser):
        parser.add_argument('tables', nargs='+', type=str)

    def handle(self, *args, **options):
        table = options['tables'][0]

        pathes = Path(f'{settings.DATA_DIR}/data/html/{table}/')
        if table in ['sire', 'bms']:
            pathes = Path(f'{settings.DATA_DIR}/data/html/stallion/')
        for path in tqdm(pathes.glob('*')):
            try:
                _id = path.stem
                soup = BeautifulSoup(open(path), 'html.parser')

                if table in ['owner', 'jockey', 'trainer', 'breeder']:
                    self.insert_human(table, _id, soup)
                elif table in ['sire', 'bms']:
                    self.insert_breed(_id, soup)
                elif table == 'horse':
                    pass
                else:
                    print('No Table')
            except Exception as e:
                print(_id)
                print(e)
