from os import execl, pipe
from django.core.management.base import BaseCommand
from django.db import models
from django.db.models import base
from race_info.models import *
from basic_info.models import *
from result.models import Race
from django.db.utils import IntegrityError

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
            try:
                p = Stallion.objects.get_or_create(id=father_id, name=breed_data[0].text)
            except:
                print(father_id, breed_data[0])
                exit()

        if bms is None:
            soup = self.get_html('stallion', mother_father_id)
            sire = Stallion.objects.filter(id=mother_father_id).first()
            try:
                p = Stallion.objects.get_or_create(id=mother_father_id, name=breed_data[4].text)
            except Exception as e:
                print(horse_id, mother_father_id, breed_data[4], breed_data[4].text)
                print(e)
                exit()

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

    def scrape_and_save(self, race_id):
        soup = BeautifulSoup(open(f'/work/data/html/race/2021/{race_id}.html'), 'html.parser')

        try:
            month = soup.find_all('title')[0].text.split('年')[1].split('月')[0].split()[0]
        except:
            return
        date = soup.find_all('title')[0].text.split('年')[1].split('月')[1].split('日')[0].split()[0]
        race_date = f'{race_id[:4]}-{month}-{date}'
        # 開催場所
        venue = Venue.objects.filter(name=soup.find_all('li', class_='Active')[0].text).first()
        # 1位賞金
        race_class = soup.find_all('div', class_='RaceData02')[0].text.split()[-1].split(':')[1].split(',')[0]
        # レース番号
        race_number = soup.find_all('span', class_='RaceNum')[0].text.split()[0].replace('R', '')
        # 馬場
        try:
            track_type = TrackType.objects.filter(
                name=soup.find_all('div', class_='RaceData01')[0].text.split()[2][0]).first()
        except:
            return
        # 距離
        distance = soup.find_all('div', class_='RaceData01')[0].text.split()[2][1:-1]
        # 馬場状態
        try:
            track_condition = TrackCondition.objects.filter(
                name=soup.find_all('span', class_=lambda value: value and value.startswith('Item'))[0].text.split(':')[
                    1]).first()
        except:
            return
        # 左右周り
        direction = Direction.objects.filter(
            name=soup.find_all('div', class_='RaceData01')[0].text.split()[3].replace('(', '').replace(')', '')).first()
        # 天気
        weather = Weather.objects.filter(
            name=soup.find_all('div', class_='RaceData01')[0].text.split()[-3].split(':')[1]).first()
        # 出走馬数
        starters = len(soup.find_all('div', class_='Rank'))
        for _rank in soup.find_all('div', class_='Rank'):
            if _rank.text == '取消' or _rank.text == '中止' or _rank.text == '除外':
                starters -= 1

        table = soup.find('table', class_='RaceTable01 RaceCommon_Table ResultRefund Table_Show_All')
        for tr in table.find_all('tr', class_='HorseList'):
            # 着順
            rank = tr.find('td', class_=lambda value: value and value.startswith('Result_Num')).text.split()[0]
            if rank.isdecimal() is False:
                continue
            # 枠
            bracket = tr.find('td', class_=lambda value: value and value.startswith('Waku')).text.split()[0]
            # 馬番
            horse_number = tr.find('td', class_=lambda value: value and value.startswith('Num Txt_C')).text.split()[0]
            # 馬ID
            horse_id = tr.find('span', class_='Horse_Name').find('a').get('href').split('/')[-1]
            horse = Horse.objects.filter(
                id=tr.find('span', class_='Horse_Name').find('a').get('href').split('/')[-1]).first()

            # horse情報なければ追加
            if horse is None:
                soup = self.get_html('horse', horse_id)
                horse_name = tr.find('span', class_='Horse_Name').find('a').get('title')
                self.scrape_and_save_horse(soup, horse_id, horse_name)
                horse = Horse.objects.filter(id=horse_id).first()

            # 性別
            gender = Gender.objects.filter(name=tr.find('span', class_='Lgt_Txt Txt_C').text.split()[0][0]).first()
            # 年齢
            age = tr.find('span', class_='Lgt_Txt Txt_C').text.split()[0][1]
            # 斤量
            jockey_weight = float(tr.find('span', class_='JockeyWeight').text.split()[0])
            # 騎手ID
            jockey_id = Jockey.objects.filter(
                id=tr.find('td', class_='Jockey').find('a').get('href').split('/')[-2]).first()
            # トレーニングセンター
            training_center = TrainingCenter.objects.filter(
                name=tr.find('td', class_='Trainer').find('span').text).first()
            # 調教師ID
            trainer_id = Trainer.objects.filter(
                id=tr.find('td', class_='Trainer').find('a').get('href').split('/')[-2]).first()

            # タイム
            race_time = tr.find('span', class_='RaceTime').text.split()[0]
            race_time = int(race_time.split(':')[0]) * 60 + float(race_time.split(':')[1])
            # 人気
            popularity = race_time = tr.find('span', class_='OddsPeople').text.split()[0]
            # オッズ
            odds = tr.find('td', class_='Odds Txt_R').text.split()[0]
            # 後3F
            three_halon = tr.find_all('td', class_='Time')[2].text.split()[0]
            # コーナー通過順
            corner_rank_1st, corner_rank_2nd, corner_rank_3rd, corner_rank_4th = 0, 0, 0, 0
            try:
                corner_rank = tr.find('td', class_='PassageRate').text.split()[0].split('-')
                if len(corner_rank) == 1:
                    corner_rank_4th = corner_rank[0]
                elif len(corner_rank) == 2:
                    corner_rank_3rd = corner_rank[0]
                    corner_rank_4th = corner_rank[1]
                elif len(corner_rank) == 3:
                    corner_rank_2nd = corner_rank[0]
                    corner_rank_3rd = corner_rank[1]
                    corner_rank_4th = corner_rank[2]
                elif len(corner_rank) == 4:
                    corner_rank_1st = corner_rank[0]
                    corner_rank_2nd = corner_rank[1]
                    corner_rank_3rd = corner_rank[2]
                    corner_rank_4th = corner_rank[3]
            except:
                pass
            # 馬体重
            horse_weight = tr.find('td', class_='Weight').text.split()[0].split('(')[0]
            # 馬体重増減
            try:
                horse_weight_change = int(tr.find('td', class_='Weight').text.split()[0].split('(')[1].replace(')', ''))
            except:
                horse_weight_change = 0

            try:
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
                    trainer=trainer_id,
                    rank=rank,
                    race_time=race_time,
                    popularity=popularity,
                    odds=odds,
                    three_halon=three_halon,
                    first_corner_rank=corner_rank_1st,
                    second_corner_rank=corner_rank_2nd,
                    third_corner_rank=corner_rank_3rd,
                    fourth_corner_rank=corner_rank_4th,
                    horse_weight=horse_weight,
                    horse_weight_change=horse_weight_change
                )
            except IntegrityError:
                print(race_id, horse_id)

    def handle(self, *args, **options):

        races = list(set(list(
            Race.objects.filter(race_date__range=["2020-01-01", "2020-08-31"]).values_list('race_id', flat=True))))
        for race_id in tqdm(races):
            # if Race.objects.filter(race_id='2021' + str(race_id)[4:]).first() is not None:
            #     continue

            print('2021' + str(race_id)[4:])
            self.scrape_and_save('2021' + str(race_id)[4:])
