import pathlib

import pandas as pd
from tqdm import tqdm

from base_scraper import BaseScraping


class BmsScraping(BaseScraping):
    def __init__(self):
        super().__init__()
        self.table_name = 't_bms'
        self.columns = [
            'bms_id', 'bms_rank',
            'bms_horse_num', 'bms_horse_win_num',
            'bms_race_num', 'bms_race_win_num',
            'bms_graded_race', 'bms_graded_race_win',
            'bms_special_race', 'bms_special_race_win',
            'bms_general_race', 'bms_general_race_win',
            'bms_turf_race', 'bms_turf_race_win',
            'bms_dirt_race', 'bms_dirt_race_win',
            'bms_win_rate', 'bms_ei', 'bms_get_prize',
            'bms_average_turf_dist', 'bms_average_dirt_dist'
        ]

    def convert_html_to_df(self):
        pass


def main():
    bms = BmsScraping()

    # html取得（過去データ）
    bms.scrape_html_past()

    # 取得したhtmlからpandas形式のデータに変換する
    bms.convert_html_to_df()

    # sqliteにデータを流し込む
    bms.to_sql(df)


if __name__ == '__main__':
    main()
