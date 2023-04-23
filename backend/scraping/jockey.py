import pathlib

import pandas as pd
from tqdm import tqdm

from base import BaseScraping


class JockeyScraping(BaseScraping):
    def __init__(self):
        super().__init__()
        self.table_name = 't_jockey'

    def convert_html_to_df(self):
        pass


def main():
    jockey = JockeyScraping()

    # html取得（過去データ）
    jockey.scrape_html_past()

    # 取得したhtmlからpandas形式のデータに変換する
    jockey.convert_html_to_df()

    # sqliteにデータを流し込む
    jockey.to_sql(df)


if __name__ == '__main__':
    main()
