import pathlib

import pandas as pd
from tqdm import tqdm

from base import BaseScraping


class BreedScraping(BaseScraping):
    def __init__(self):
        super().__init__()
        self.table_name = 't_breed'
        self.columns = [
            'breed_id', 'breed_rank',
            'breed_horse_num', 'breed_horse_win_num',
            'breed_race_num', 'breed_race_win_num',
            'breed_graded_race', 'breed_graded_race_win',
            'breed_special_race', 'breed_special_race_win',
            'breed_general_race', 'breed_general_race_win',
            'breed_turf_race', 'breed_turf_race_win',
            'breed_dirt_race', 'breed_dirt_race_win',
            'breed_win_rate', 'breed_ei', 'breed_get_prize',
            'breed_average_turf_dist', 'breed_average_dirt_dist'
        ]

    def convert_html_to_df(self):
        pass


def main():
    breed = BreedScraping()

    # 取得対象のhorse_id取得
    

    # html取得
    breed.scrape_html_past()

    # 取得したhtmlからpandas形式のデータに変換する
    breed.convert_html_to_df()

    # sqliteにデータを流し込む
    breed.to_sql(df)


if __name__ == '__main__':
    main()