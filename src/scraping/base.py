import sqlite3
import requests
import time

from bs4 import BeautifulSoup


class BaseScraping():
    def __init__(self):
        self.db_path = 'data/central.db'
        self.table_name = ''

    def scrape_html_realtime(self, url, use_webdriver=False):
        time.sleep(1)

        if use_webdriver:
            PATH = '/mnt/d/Downloads/chromedriver_win32/chromedriver.exe'

            driver = webdriver.Chrome(executable_path=PATH)
            WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located)
            driver.get(url)
            html = driver.page_source
            driver.close()

            return BeautifulSoup(html, 'html.parser')
        else:
            return self.scrape_html(url)

    def scrape_html(self, url):
        time.sleep(1)

        html = requests.get(url)
        html.encoding = 'EUC-JP'
        return BeautifulSoup(html.text, 'html.parser')

    def scrape_html_local(self, path):
        return BeautifulSoup(open(path), 'html.parser')

    def save_html(self, target, target_id, soup, zfill=5):
        _id = str(target_id.zfill(zfill))
        with open(f'data/html/{target}/{str(_id)}.html', 'w') as f:
            f.write(str(soup))

    def to_sql(self, df, if_exists='append'):
        with sqlite3.connect(self.db_path) as conn:
            df.to_sql(self.table_name, con=conn, if_exists=if_exists, index=False)
