import pathlib

import pandas as pd
from tqdm import tqdm
import sqlite3

from base_scraper import BaseScraping


class OwnerScraping(BaseScraping):
    def __init__(self):
        super().__init__()
        self.table_name = 't_owner'
        self.columns = [
            'owner_id', 'year', 'owner_year_rank',
            'owner_year_1st', 'owner_year_2nd', 'owner_year_3rd', 'owner_year_4th',
            'owner_year_graded_race', 'owner_year_graded_race_win',
            'owner_year_special_race', 'owner_year_special_race_win',
            'owner_year_general_race', 'owner_year_general_race_win',
            'owner_year_turf_race', 'owner_year_turf_race_win',
            'owner_year_dirt_race', 'owner_year_dirt_race_win',
            'owner_year_win_rate', 'owner_year_1st_or_2nd_rate',
            'owner_year_show_rate', 'owner_year_get_prize',
            'owner_total_1st', 'owner_total_2nd', 'owner_total_3rd', 'owner_total_4th',
            'owner_total_graded_race', 'owner_total_graded_race_win',
            'owner_total_special_race', 'owner_total_special_race_win',
            'owner_total_general_race', 'owner_total_general_race_win',
            'owner_total_turf_race', 'owner_total_turf_race_win',
            'owner_total_dirt_race', 'owner_total_dirt_race_win',
            'owner_total_win_rate', 'owner_total_1st_or_2nd_rate',
            'owner_total_show_rate', 'owner_total_get_prize'
        ]

    def convert_html_to_df(self, soup, owner_id):
        # 表取得
        tables = soup.find_all('tr')
        # 累計
        for table in tables:
            if table.find('td') is None:
                continue
            if table.find('td').text == '累計':
                total_info = [data.text.replace(',', '') if data.text != '' and data.text[
                    0] != '.' else data.text.replace(
                    '.', '0.') for data in table.find_all('td')][2:-1]
                break

        # 各年度
        owner_info = []
        for table in tables:
            if table.find('td') is None:
                continue
            if table.find('td').text.isdecimal() and int(table.find('td').text) < 2011:
                break

            if table.find('td').text.isdecimal() and int(table.find('td').text) >= 2011:
                each_info = [owner_id, int(table.find('td').text) + 1]
                each_info.extend(
                    [data.text.replace(',', '') if data.text != '' and data.text[0] != '.' else data.text.replace(
                        '.', '0.') for data in table.find_all('td')][1:-1])
                each_info.extend(total_info)
                owner_info.append(each_info)

        return owner_info

    def read_ids(self):
        sql = '''
            SELECT t_horse_base.owner_id
            FROM t_race
            LEFT JOIN  t_horse_base
            ON 	t_race.horse_id = t_horse_base.horse_id
            WHERE
                t_race.race_class = 700;
        '''
        with sqlite3.connect(self.db_path) as conn:
            owner_ids = list(pd.read_sql_query(sql, conn)['owner_id'])

        return owner_ids

    def read_and_save_html(self, owner_ids):
        for owner_id in tqdm(set(owner_ids)):
            url = 'https://db.netkeiba.com/owner/result/' + str(owner_id)
            # html取得
            soup = self.scrape_html(url)
            # html保存
            self.save_html('owner', owner_id, soup, zfill=7)


def main():
    owner = OwnerScraping()

    owner_list = []
    for path in tqdm(pathlib.Path('data/html/owner/').glob('*.html')):
        soup = owner.scrape_html_local(path)
        # 取得したhtmlからpandas形式のデータに変換する
        owner_info = owner.convert_html_to_df(soup, str(path).split('/')[-1].split('.')[0][1:])
        owner_list.extend(owner_info)

    # sqliteにデータを流し込む
    df = pd.DataFrame(owner_list, columns=owner.columns)
    owner.to_sql(df, if_exists='fail')


if __name__ == '__main__':
    main()
