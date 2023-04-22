from django.core.management.base import BaseCommand
from django.conf import settings

from basic_info.models import Owner, Jockey, Trainer
from predict.models import Race, RaceRealtime, HorseBase

from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm

import time
import requests


class Command(BaseCommand):

    def get_html(self, url):
        time.sleep(1)

        html = requests.get(url)
        html.encoding = 'EUC-JP'
        return BeautifulSoup(html.text, 'html.parser')

    def add_arguments(self, parser):
        parser.add_argument('tables', nargs='+', type=str)
        parser.add_argument('id', nargs='+', type=str)

    def handle(self, *args, **options):
        table = options['tables'][0]
        _id = options['id'][0]

        if table == 'stallion':
            _url = 'https://db.netkeiba.com/horse/sire/' + _id
            soup = self.get_html(_url)
            with open(f'/work/data/html/stallion/{_id}.html', 'w') as f:
                f.write(str(soup))

        else:
            print('No Table')
