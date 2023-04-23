import time

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def get_html(self, url):
        time.sleep(1)

        html = requests.get(url)
        html.encoding = 'EUC-JP'
        return BeautifulSoup(html.text, 'html.parser')

    def save_html(self, soup, file_path):
        with open(file_path, 'w') as f:
            f.write(str(soup))

    def add_arguments(self, parser):
        parser.add_argument('tables', nargs='+', type=str)
        parser.add_argument('id', nargs='+', type=str)

    def handle(self, *args, **options):
        table = options['tables'][0]
        _id = options['id'][0]

        if table == 'stallion':
            _url = f'https://db.netkeiba.com/horse/sire/{_id}'
            soup = self.get_html(_url)
            self.save_html(soup, f'/work/data/html/stallion/{_id}.html')
        else:
            print('No Table')
