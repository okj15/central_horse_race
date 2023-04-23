from django.core.management.base import BaseCommand
from django.conf import settings

from ...models import Owner, Jockey, Trainer, Breeder, Stallion, Horse

from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm


class Command(BaseCommand):

    def insert_horse(self, _id, name, soup):
        # 共通
        base_data = soup.find('table', class_='db_prof_table')

        # 誕生日
        birth_year = base_data.find('td').text.split('年')[0]
        birth_month = base_data.find('td').text.split('年')[1].split('月')[0]
        birth_date = base_data.find('td').text.split('月')[1].split('日')[0]

        birthday = f'{birth_year}-{birth_month.zfill(2)}-{birth_date.zfill(2)}'

        # 馬主ID, ブリーダーID, 通算成績
        owner_id = ''
        breeder_id = ''
        for data in base_data.find_all('a'):
            if data.get('href') and '/owner/' in data.get('href'):
                owner_id = data.get('href').split('/')[-2]
            if data.get('href') and '/breeder/' in data.get('href'):
                breeder_id = data.get('href').split('/')[-2]

        owner = Owner.objects.filter(id=owner_id).first()
        breeder = Breeder.objects.filter(id=breeder_id).first()

        # 血統
        breed_data = soup.find('table', class_='blood_table').find_all('a')
        father_id = breed_data[0].get('href').split('/')[-2]
        father_father_id = breed_data[1].get('href').split('/')[-2]
        father_mother_id = breed_data[2].get('href').split('/')[-2]
        mother_id = breed_data[3].get('href').split('/')[-2]
        mother_father_id = breed_data[4].get('href').split('/')[-2]
        mother_mother_id = breed_data[5].get('href').split('/')[-2]

        sire = Stallion.objects.filter(id=father_id).first()
        bms = Stallion.objects.filter(id=mother_father_id).first()

        p = Horse.objects.update_or_create(
            id=_id,
            name=name,
            birthday=birthday,
            owner=owner,
            breeder=breeder,
            father=sire,
            mother=mother_id,
            father_father=father_father_id,
            father_mother=father_mother_id,
            mother_father=bms,
            mother_mother=mother_mother_id
        )


    def add_arguments(self, parser):
        parser.add_argument('tables', nargs='+', type=str)
        parser.add_argument('id', nargs='+', type=str)

    def handle(self, *args, **options):
        table = options['tables'][0]
        _id = options['id'][0]

        path = Path(f'{settings.DATA_DIR}/data/html/{table}/{_id}.html')
        try:
            soup = BeautifulSoup(open(path), 'html.parser')
            title = soup.find('title').contents[0]
            if 'の' in title:
                name = title.split('の')[0]
            else:
                name = title.split(' ')[0]

            if table == 'owner':
                p = Owner.objects.update_or_create(id=_id, name=name)
            elif table == 'jockey':
                p = Jockey.objects.update_or_create(id=_id, name=name)
            elif table == 'trainer':
                p = Trainer.objects.update_or_create(id=_id, name=name)
            elif table == 'breeder':
                p = Breeder.objects.update_or_create(id=_id, name=name)
            elif table == 'stallion':
                p = Stallion.objects.update_or_create(id=_id, name=name)
            elif table == 'horse':
                self.insert_horse(_id, name, soup)
            else:
                print('No Table')
        except Exception as e:
            print(_id)
            print(e)
