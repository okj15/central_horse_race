import pathlib
import sqlite3

import pandas as pd
from tqdm import tqdm

from base import BaseScraping


class HorseScraping(BaseScraping):
    def __init__(self):
        super().__init__()


def main():
    horse = HorseScraping()

    sql = '''
        SELECT DISTINCT race_realtime.horse_id
            FROM race_realtime
                LEFT JOIN basic_info_horse
                ON
                    race_realtime.horse_id = basic_info_horse.id
            WHERE
					basic_info_horse.id is NULL;
    '''

    with sqlite3.connect(horse.db_path) as conn:
        horse_ids = list(pd.read_sql_query(sql, conn)['horse_id'])

    # html取得（過去データ）
    base_list = []
    for horse_id in tqdm(horse_ids):
        url = 'https://db.netkeiba.com/horse/' + str(horse_id)
        soup = horse.scrape_html(url)

        with open(f'/work/data/html/horse/{horse_id}.html', 'w') as f:
            f.write(str(soup))


if __name__ == '__main__':
    main()
