import os
import time

import requests
from bs4 import BeautifulSoup
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseScraper(object):

    def __init__(self, app_name, target_id):
        self.app_name = app_name
        self.target_id = target_id
        self.local_path = f'/work/data/html/{self.app_name}/{self.target_id}.html'
        self.scrape_url = f'{settings.SCRAPE_URL}{self.app_name}/result/{self.target_id}'

    def _sleep(self):
        """
        スクレイピングの間隔をあける
        :return:
        """
        time.sleep(1)

    def _get_html_from_url(self, url):
        """
        URLからHTMLを取得
        :param url:
        :return:
        """
        self._sleep()
        html = requests.get(url)
        html.encoding = 'EUC-JP'
        return BeautifulSoup(html.text, 'html.parser')

    def _get_html_from_webdriver(self, url, webdriver_path):
        """
        URLからHTMLを取得
        :param url:
        :param webdriver_path:
        :return:
        """
        self._sleep()
        driver = webdriver.Chrome(executable_path=webdriver_path)
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located)
        driver.get(url)
        html = driver.page_source
        driver.close()

        return BeautifulSoup(html, 'html.parser')

    def scrape_html_realtime(self, use_webdriver=False, webdriver_path=None):
        """
        リアルタイムにHTMLを取得
        :param use_webdriver:
        :param webdriver_path:
        :return:
        """
        if use_webdriver:
            if webdriver_path is None:
                raise ValueError('webdriver_path is required when use_webdriver is True.')
            return self._get_html_from_webdriver(self.scrape_url, webdriver_path)

        return self._get_html_from_url(self.scrape_url)

    def scrape_html(self, use_webdriver=False, webdriver_path=None):
        """
        HTMLを取得
        :param webdriver_path: bool
        :param use_webdriver: str
        :return:
        """
        # 対象パスが存在するかチェック
        if os.path.exists(self.local_path):
            return self.scrape_html_local(self.local_path)

        # リアルタイムな情報を取得する場合は、webdriverを使用する
        if use_webdriver:
            if webdriver_path is None:
                raise ValueError('webdriver_path is required when use_webdriver is True.')
            soup = self._get_html_from_webdriver(self.scrape_url, webdriver_path)
        else:
            soup = self._get_html_from_url(self.scrape_url)

        self.save_html(soup)

        return soup

    def scrape_html_local(self, path):
        """
        ローカルのHTMLを取得
        :param path:
        :return:
        """
        return BeautifulSoup(open(path), 'html.parser')

    def save_html(self, soup):
        """
        HTMLを保存
        :param soup:
        :return:
        """
        with open(self.local_path, 'w') as f:
            f.write(str(soup))
