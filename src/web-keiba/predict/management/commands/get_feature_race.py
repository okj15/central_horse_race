from os import pipe
from django.core.management.base import BaseCommand
from race_info.models import *
from basic_info.models import *
from result.models import Race

import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class Command(BaseCommand):

    def get_html(self, target, _id, url=''):
        time.sleep(1)
        if not url:
            url = f'https://db.netkeiba.com/{target}/{_id}'
        html = requests.get(url)
        html.encoding = 'EUC-JP'
        soup = BeautifulSoup(html.text, 'html.parser')
        with open(f'/work/data/html/{target}/{_id}.html', 'w') as f:
                f.write(str(soup))

        return soup

    def get_race_html(self, base_url, base_race_id):
        for i in tqdm(range(1, 13)):
            race_id = base_race_id + str(i).zfill(2)
            url = base_url + race_id
            time.sleep(1)
            html = requests.get(url)
            html.encoding = 'EUC-JP'
            soup = BeautifulSoup(html.text, 'html.parser')
            with open(f'/work/data/html/race/2021/{race_id}.html', 'w') as f:
                    f.write(str(soup))

    def scrape_and_save_horse(self, soup, horse_id, horse_name):
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

        if sire is None:
            soup = self.get_html('stallion', father_id)
            sire = Stallion.objects.filter(id=father_id).first()
            p = Stallion.objects.get_or_create(id=father_id, name=breed_data[0].text)

        if bms is None:
            soup = self.get_html('stallion', mother_father_id)
            sire = Stallion.objects.filter(id=mother_father_id).first()
            p = Stallion.objects.get_or_create(id=mother_father_id, name=breed_data[4].text)

        p = Horse.objects.update_or_create(
            id=horse_id,
            name=horse_name,
            birthday=birthday,
            owner=owner,
            breeder=breeder,
            father=sire,
            mother_id=mother_id,
            father_father_id=father_father_id,
            father_mother_id=father_mother_id,
            mother_father=bms,
            mother_mother_id=mother_mother_id
        )

    def scrape_and_save(self, base_race_id):
        for i in tqdm(range(1, 13)):
            race_id = base_race_id + str(i).zfill(2)
            soup = BeautifulSoup(open(f'/work/data/html/race/2021/{race_id}.html'), 'html.parser')

            month = soup.find_all('title')[0].text.split('年')[1].split('月')[0].split()[0]
            date = soup.find_all('title')[0].text.split('月')[1].split('日')[0].split()[0]
            race_date = f'{race_id[:4]}-{month}-{date}'
            # 開催場所
            venue = Venue.objects.filter(name=soup.find_all('li', class_='Active')[0].text).first()
            # 1位賞金
            race_class = soup.find_all('div', class_='RaceData02')[0].text.split()[-1].split(':')[1].split(',')[0]
            # レース番号
            race_number = soup.find_all('span', class_='RaceNum')[0].text.split()[0].replace('R', '')
            # 馬場
            track_type =  TrackType.objects.filter(name=soup.find_all('div', class_='RaceData01')[0].text.split()[2][0]).first()
            # 距離
            distance = soup.find_all('div', class_='RaceData01')[0].text.split()[2][1:-1]
            # 馬場状態
            track_condition = TrackCondition.objects.filter(name=soup.find_all('span', class_=lambda value: value and value.startswith('Item'))[0].text.split(':')[1]).first()
            # 左右周り
            direction = Direction.objects.filter(name=soup.find_all('div', class_='RaceData01')[0].text.split()[3].replace('(', '').replace(')', '')).first()
            # 天気
            weather = Weather.objects.filter(name=soup.find_all('div', class_='RaceData01')[0].text.split()[-3].split(':')[1]).first()
            # 出走馬数
            starters = len(soup.find('table', class_='Shutuba_Table').find_all('span', class_='HorseName')) - 1

            table = soup.find('table', class_='Shutuba_Table')
            for tr in table.find_all('tr', class_='HorseList'):
                # 取消の場合次へ進む
                if tr.find('td', class_='Cancel_Txt'):
                    continue

                # 枠
                bracket = tr.find('td', class_=lambda value: value and value.startswith('Waku')).text.split()[0]
                # 馬番
                horse_number = tr.find('td', class_=lambda value: value and value.startswith('Umaban')).text.split()[0]
                # 馬ID
                horse_id = tr.find('span', class_='HorseName').find('a').get('href').split('/')[-1]
                horse = Horse.objects.filter(id=tr.find('span', class_='HorseName').find('a').get('href').split('/')[-1]).first()

                # horse情報なければ追加
                if horse is None:
                    soup = self.get_html('horse', horse_id)
                    horse_name = tr.find('span', class_='HorseName').find('a').get('title')
                    self.scrape_and_save_horse(soup, horse_id, horse_name)
                    horse = Horse.objects.filter(id=horse_id).first()

                # 性別
                gender = Gender.objects.filter(name=tr.find('td', class_='Barei Txt_C').text.split()[0][0]).first()
                # 年齢
                age = tr.find('td', class_='Barei Txt_C').text.split()[0][1]
                # 斤量
                jockey_weight = float(tr.select("[class='Txt_C']")[0].text)
                # 騎手ID
                jockey_id = Jockey.objects.filter(id=tr.find('td', class_='Jockey').find('a').get('href').split('/')[-2]).first()
                # トレーニングセンター
                training_center = TrainingCenter.objects.filter(name=tr.find('td', class_='Trainer').find('span').text).first()
                # 調教師ID
                trainer_id = Trainer.objects.filter(id=tr.find('td', class_='Trainer').find('a').get('href').split('/')[-2]).first()

                Race.objects.update_or_create(
                    race_id=race_id,
                    race_date=race_date,
                    venue=venue,
                    race_class=race_class,
                    race_number=race_number,
                    track_type=track_type,
                    distance=distance,
                    track_condition=track_condition,
                    direction=direction,
                    weather=weather,
                    starters=starters,
                    bracket=bracket,
                    horse_number=horse_number,
                    horse=horse,
                    gender=gender,
                    age=age,
                    jockey_weight=jockey_weight,
                    jockey=jockey_id,
                    training_center=training_center,
                    trainer=trainer_id
                )                

    def add_arguments(self, parser):
        parser.add_argument('base_race_id', nargs='+', type=str)

    def handle(self, *args, **options):
        base_race_id = options['base_race_id'][0]

        base_url = 'https://race.netkeiba.com/race/shutuba.html?race_id='

        # レースHTML取得 & 保存
        self.get_race_html(base_url, base_race_id)

        # スクレイプ & DB保存
        self.scrape_and_save(base_race_id)