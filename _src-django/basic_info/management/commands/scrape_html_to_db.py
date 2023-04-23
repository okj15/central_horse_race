from pathlib import Path

from bs4 import BeautifulSoup
from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Owner, Jockey, Trainer, Breeder, Stallion, Horse


class Command(BaseCommand):
    """
    HTMLをDBに登録する
    """

    def _get_birthdate(self, base_data):
        """
        誕生日を取得
        :param base_data:
        :return:
        """
        birth_year = base_data.find('td').text.split('年')[0]
        birth_month = base_data.find('td').text.split('年')[1].split('月')[0]
        birth_date = base_data.find('td').text.split('月')[1].split('日')[0]
        return f'{birth_year}-{birth_month.zfill(2)}-{birth_date.zfill(2)}'

    def _get_owner_and_breeder_id(self, base_data):
        """
        馬主ID, ブリーダーIDを取得
        :param base_data:
        :return:
        """
        owner_id, breeder_id = '', ''
        for data in base_data.find_all('a'):
            href = data.get('href')
            if href:
                if '/owner/' in href:
                    owner_id = href.split('/')[-2]
                elif '/breeder/' in href:
                    breeder_id = href.split('/')[-2]
        return owner_id, breeder_id

    def get_breed_data(self, breed_data_table):
        """
        血統情報を取得
        :param breed_data_table:
        :return:
        """
        breed_data = breed_data_table.find_all('a')
        return [data.get('href').split('/')[-2] for data in breed_data]

    def insert_horse(self, _id, name, soup):
        """
        馬情報を登録
        :param _id:
        :param name:
        :param soup:
        :return:
        """
        # 共通
        base_data = soup.find('table', class_='db_prof_table')

        # 誕生日
        birthday = self.get_birthdate(base_data)

        # 馬主ID, ブリーダーID
        owner_id, breeder_id = self._get_owner_and_breeder_id(base_data)

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

        Horse.objects.update_or_create(
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
            name = title.split('の')[0] if 'の' in title else title.split(' ')[0]

            model = {
                'owner': Owner,
                'jockey': Jockey,
                'trainer': Trainer,
                'breeder': Breeder,
                'stallion': Stallion,
            }.get(table)

            if model:
                if table == 'horse':
                    self.insert_horse(_id, name, soup)
                else:
                    model.objects.update_or_create(id=_id, name=name)
            else:
                print('No Table')

        except Exception as e:
            print(_id)
            print(e)
