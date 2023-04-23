import pathlib
import sqlite3

import pandas as pd
from tqdm import tqdm

from base_scraper import BaseScraping


class HorseScraping(BaseScraping):
    def __init__(self):
        super().__init__()
        self.table_name = 'horse_base'

        self.columns = [
            'horse_id', 'birth_year', 'birth_month', 'birth_date',
            'owner_id', 'breeder_id',
            'father_id', 'father_father_id', 'father_mother_id',
            'mother_id', 'mother_father_id', 'mother_mother_id',
        ]

    def convert_html_to_df(self, soup, horse_id):
        # 共通
        base_data = soup.find('table', class_='db_prof_table')

        # 誕生日
        birth_year = base_data.find('td').text.split('年')[0]
        birth_month = base_data.find('td').text.split('年')[1].split('月')[0]
        birth_date = base_data.find('td').text.split('月')[1].split('日')[0]

        # 馬主ID, ブリーダーID, 通算成績
        owner_id = ''
        breeder_id = ''
        for data in base_data.find_all('a'):
            if data.get('href') and '/owner/' in data.get('href'):
                owner_id = data.get('href').split('/')[-2]
            if data.get('href') and '/breeder/' in data.get('href'):
                breeder_id = data.get('href').split('/')[-2]

        # 血統
        breed_data = soup.find('table', class_='blood_table').find_all('a')
        father_id = breed_data[0].get('href').split('/')[-2]
        father_father_id = breed_data[1].get('href').split('/')[-2]
        father_mother_id = breed_data[2].get('href').split('/')[-2]
        mother_id = breed_data[3].get('href').split('/')[-2]
        mother_father_id = breed_data[4].get('href').split('/')[-2]
        mother_mother_id = breed_data[5].get('href').split('/')[-2]

        base_info = [
            horse_id, birth_year, birth_month, birth_date,
            owner_id, breeder_id,
            father_id, father_father_id, father_mother_id,
            mother_id, mother_father_id, mother_mother_id
        ]

        return [base_info]


def main():
    horse = HorseScraping()

    sql = '''
        SELECT DISTINCT race_realtime.horse_id
            FROM race_realtime
                LEFT JOIN horse_base
                ON
                    race_realtime.horse_id = horse_base.horse_id
            WHERE
                race_realtime.race_class = 700 AND father_id is NULL;
    '''

    with sqlite3.connect(horse.db_path) as conn:
        horse_ids = list(pd.read_sql_query(sql, conn)['horse_id'])

    # html取得（過去データ）
    base_list = []
    for horse_id in tqdm(horse_ids):
        url = 'https://db.netkeiba.com/horse/' + str(horse_id)
        soup = horse.scrape_html(url)

        # 取得したhtmlからpandas形式のデータに変換する
        base_info = horse.convert_html_to_df(soup, horse_id)
        base_list.extend(base_info)

    # sqliteにデータを流し込む
    df = pd.DataFrame(base_list, columns=horse.columns)
    horse.to_sql(df)


if __name__ == '__main__':
    main()
