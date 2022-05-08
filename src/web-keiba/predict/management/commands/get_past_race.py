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
            url = f'https://db.netkeiba.com/{target}/{_id}.html'
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

    def scrape_and_save(self, base_race_id):
        for i in tqdm(range(1, 13)):
            race_id = base_race_id + str(i).zfill(2)
            soup = BeautifulSoup(open(f'/work/data/html/race/2021/{race_id}.html'), 'html.parser')

            # 馬場状態
            track_condition = TrackCondition.objects.filter(name=soup.find_all('span', class_=lambda value: value and value.startswith('Item'))[0].text.split(':')[1]).first()
            # 天気
            weather = Weather.objects.filter(name=soup.find_all('div', class_='RaceData01')[0].text.split()[-3].split(':')[1]).first()

            table = soup.find('table', class_='RaceTable01 RaceCommon_Table ResultRefund Table_Show_All')
            for tr in table.find_all('tr', class_='HorseList'):
                rank = tr.find('td', class_=lambda value: value and value.startswith('Result_Num')).text.split()[0]
                if rank.isdecimal() is False:
                    continue

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

                # タイム
                race_time = tr.find('span', class_='RaceTime').text.split()[0]
                race_time = int(race_time.split(':')[0]) * 60 + float(race_time.split(':')[1])

                # 馬ID
                horse_id = tr.find('span', class_='Horse_Name').find('a').get('href').split('/')[-1]
                horse = Horse.objects.filter(id=horse_id).first()

                Race.objects.update_or_create(
                    race_id=race_id,
                    horse = horse,
                    defaults={
                        'track_condition': track_condition,
                        'weather': weather,
                        'rank': rank,
                        'popularity': popularity,
                        'odds': odds,
                        'three_halon': three_halon,
                        'first_corner_rank': corner_rank_1st,
                        'second_corner_rank': corner_rank_2nd,
                        'third_corner_rank': corner_rank_3rd,
                        'fourth_corner_rank': corner_rank_4th,
                        'horse_weight': horse_weight,
                        'horse_weight_change': horse_weight_change,
                        'race_time': race_time
                    }
                )                

    def add_arguments(self, parser):
        parser.add_argument('base_race_id', nargs='+', type=str)

    def handle(self, *args, **options):
        base_race_id = options['base_race_id'][0]

        base_url = 'https://race.netkeiba.com/race/result.html?race_id='

        # レースHTML取得 & 保存
        self.get_race_html(base_url, base_race_id)

        # スクレイプ & DB保存
        self.scrape_and_save(base_race_id)