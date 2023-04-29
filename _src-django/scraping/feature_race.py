import pathlib

import pandas as pd
from tqdm import tqdm

from base import BaseScraping


def convert_place_to_number(place):
    place_dict = {
        '函館': 0,
        '札幌': 1,
        '小倉': 2,
        '福島': 3,
        '中京': 4,
        '新潟': 5,
        '京都': 6,
        '東京': 7,
        '阪神': 8,
        '中山': 9
    }

    return place_dict.get(place, -1)


def convert_field_to_number(field):
    field_dict = {
        '芝': 0,
        'ダ': 1
    }

    return field_dict.get(field, -1)


def convert_field_condition_to_number(field_condition):
    field_condition_dict = {
        '良': 0,
        '稍': 1,
        '重': 2,
        '不': 3
    }

    return field_condition_dict.get(field_condition, -1)


def convert_l_or_r_to_number(l_or_r):
    if '右' in l_or_r:
        l_or_r_number = 0
    elif '左' in l_or_r:
        l_or_r_number = 1
    else:
        l_or_r_number = -1

    return l_or_r_number


def convert_weather_to_number(weather):
    weather_dict = {
        '晴': 0,
        '曇': 1,
        '小雨': 2,
        '小雪': 3,
        '雨': 4,
        '雪': 5
    }

    return weather_dict.get(weather, -1)


def convert_gender_to_numeber(gender):
    gender_dict = {
        '牡': 0,
        '牝': 1,
        'セ': 2
    }

    return gender_dict.get(gender, -1)


def convert_jockey_info(jockey_name):
    jocky_symbol_dict = {
        '☆': 1,
        '△': 2,
        '▲': 3,
        '★': 4
    }
    jockey_symbol = jocky_symbol_dict.get(jockey_name[0], 0)
    if jockey_symbol != 0:
        jockey_name = jockey_name[1:]

    return jockey_name, jockey_symbol


def convert_training_center_to_number(training_center):
    training_center_dict = {
        '栗東': 0,
        '美浦': 1
    }

    return training_center_dict.get(training_center, -1)


class FeatureRaceScraping(BaseScraping):
    def __init__(self):
        super().__init__()
        self.table_name = 'race_realtime'
        self.columns = [
            'race_id', 'year', 'month', 'date', 'place', 'race_class', 'race_number', 'field', 'dist',
            'field_condition', 'l_or_r', 'weather', 'starters_number',
            'rank', 'waku', 'horse_number', 'horse_id', 'horse_name', 'gender', 'age',
            'jockey_weight', 'jockey_id', 'jockey_name', 'race_time', 'popularity', 'odds',
            'training_center', 'trainer_id', 'trainer_name', 'horse_weight', 'horse_weight_change'
        ]

    def convert_html_to_df(self, soup, year, race_id):
        # 月
        month = soup.find_all('title')[0].text.split('年')[1].split('月')[0].split()[0]
        # 日
        date = soup.find_all('title')[0].text.split('月')[1].split('日')[0].split()[0]
        # 開催場所
        place = convert_place_to_number(soup.find_all('li', class_='Active')[0].text)
        # 1位賞金
        race_class = soup.find_all('div', class_='RaceData02')[0].text.split()[-1].split(':')[1].split(',')[0]
        # レース番号
        race_number = soup.find_all('span', class_='RaceNum')[0].text.split()[0].replace('R', '')
        # 馬場
        field = convert_field_to_number(soup.find_all('div', class_='RaceData01')[0].text.split()[2][0])
        # 距離
        dist = soup.find_all('div', class_='RaceData01')[0].text.split()[2][1:-1]
        # 馬場状態
        field_condition = convert_field_condition_to_number(
            soup.find_all('span', class_=lambda value: value and value.startswith('Item'))[0].text.split(':')[1])
        # 左右周り
        l_or_r = convert_l_or_r_to_number(
            soup.find_all('div', class_='RaceData01')[0].text.split()[3].replace('(', '').replace(')', ''))
        # 天気
        weather = convert_weather_to_number(soup.find_all('div', class_='RaceData01')[0].text.split()[-3].split(':')[1])
        # 出走馬数
        starters_number = len(soup.find('table', class_='Shutuba_Table').find_all('span', class_='HorseName')) - 1

        # starters_number -= len(soup.find_all('td', class_='Cancel_Txt'))

        race_info = []
        table = soup.find('table', class_='Shutuba_Table')
        for tr in table.find_all('tr', class_='HorseList'):

            # 取消の場合次へ進む
            if tr.find('td', class_='Cancel_Txt'):
                continue

            # 着順
            rank = 0
            # 枠
            waku = tr.find('td', class_=lambda value: value and value.startswith('Waku')).text.split()[0]
            # 馬番
            horse_number = tr.find('td', class_=lambda value: value and value.startswith('Umaban')).text.split()[0]
            # 馬ID
            horse_id = tr.find('span', class_='HorseName').find('a').get('href').split('/')[-1]
            # 馬名
            horse_name = tr.find('span', class_='HorseName').find('a').get('title')
            # 性別
            gender = convert_gender_to_numeber(tr.find('td', class_='Barei Txt_C').text.split()[0][0])
            # 年齢
            age = tr.find('td', class_='Barei Txt_C').text.split()[0][1]
            # 斤量
            jockey_weight = tr.select("[class='Txt_C']")[0].text
            # 騎手ID
            jockey_id = tr.find('td', class_='Jockey').find('a').get('href').split('/')[-2]
            # 騎手名
            jockey_name = tr.find('td', class_='Jockey').text.split()[0]
            jockey_name, jockey_symbol = convert_jockey_info(jockey_name)
            # タイム
            race_time = '0'
            # 人気
            popularity = tr.find('span', id=lambda value: value and value.startswith('ninki')).text.split()[0]
            # 単勝オッズ
            odds = tr.find('td', class_='Txt_R Popular').text.split()[0]
            # トレーニングセンター
            training_center = convert_training_center_to_number(tr.find('td', class_='Trainer').find('span').text)
            # 調教師ID
            trainer_id = tr.find('td', class_='Trainer').find('a').get('href').split('/')[-2]
            # 調教師
            trainer_name = tr.find('td', class_='Trainer').find('a').text
            # 馬体重
            try:
                horse_weight = tr.find('td', class_='Weight').text.split()[0].split('(')[0]
            except:
                horse_weight = 0
            # 馬体重増減
            try:
                horse_weight_change = int(tr.find('td', class_='Weight').text.split()[0].split('(')[1].replace(')', ''))
            except:
                horse_weight_change = 0

            horse_info = [
                race_id, year, month, date, place, race_class, race_number, field, dist, field_condition,
                l_or_r, weather, starters_number,
                rank, waku, horse_number, horse_id, horse_name, gender, age, jockey_weight,
                jockey_id, jockey_name, race_time, popularity, odds,
                training_center, trainer_id, trainer_name, horse_weight, horse_weight_change
            ]

            race_info.append(horse_info)

        return race_info


def main():
    feature_race = FeatureRaceScraping()

    race_list = []
    base_url = 'https://race.netkeiba.com/race/shutuba.html?race_id='
    for race_id in ['202104030405', '202104030406', '202102011005']:
        url = base_url + race_id
        # html取得
        soup = feature_race.scrape_html(url)

        # html保存
        with open(f'data/html/race_realtime/20210801/{race_id}.html', 'w') as f:
            f.write(str(soup))

        # 取得したhtmlからpandas形式のデータに変換する
        race_info = feature_race.convert_html_to_df(soup, '2021', race_id)
        race_list.extend(race_info)

    # sqliteにデータを流し込む
    df = pd.DataFrame(race_list, columns=feature_race.columns)
    feature_race.to_sql(df)


if __name__ == '__main__':
    main()
