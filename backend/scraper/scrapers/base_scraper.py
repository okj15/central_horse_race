import sqlite3
import time

import requests
from bs4 import BeautifulSoup
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseScraping(object):
    def __init__(self, db_path=settings.DATABASES['default']['NAME'], table_name=''):
        self.db_path = db_path
        self.table_name = table_name

    def _sleep(self):
        time.sleep(1)

    def _get_html_from_url(self, url):
        self._sleep()
        html = requests.get(url)
        html.encoding = 'EUC-JP'
        return BeautifulSoup(html.text, 'html.parser')

    def _get_html_from_webdriver(self, url, webdriver_path):
        self._sleep()
        driver = webdriver.Chrome(executable_path=webdriver_path)
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located)
        driver.get(url)
        html = driver.page_source
        driver.close()

        return BeautifulSoup(html, 'html.parser')

    def scrape_html_realtime(self, url, use_webdriver=False, webdriver_path=None):
        if use_webdriver:
            if webdriver_path is None:
                raise ValueError('webdriver_path is required when use_webdriver is True.')
            html = self._get_html_from_webdriver(url, webdriver_path)
        else:
            html = self._get_html_from_url(url)

        return html

    def scrape_html(self, url):
        return self._get_html_from_url(url)

    def scrape_html_local(self, path):
        return BeautifulSoup(open(path), 'html.parser')

    def save_html(self, target, target_id, soup, zfill=5):
        _id = str(target_id.zfill(zfill))
        with open(f'data/html/{target}/{_id}.html', 'w') as f:
            f.write(str(soup))

    def to_sql(self, df, if_exists='append'):
        with sqlite3.connect(self.db_path) as conn:
            df.to_sql(self.table_name, con=conn, if_exists=if_exists, index=False)
