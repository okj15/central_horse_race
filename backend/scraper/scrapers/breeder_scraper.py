from scraper.scrapers.base_scraper import BaseScraper
from breeder.models import BreederResult


class BreederResultScraper(BaseScraper):
    APP_NAME = 'breeder'

    def parse_soup(self, soup):
        # 表取得
        tables = soup.find_all('tr')

        results = []
        for table in tables:
            if table.find('td') is None:
                continue

            # 年度別成績のみ取得（累計は除外）
            if table.find('td').text.isdecimal():
                result = []
                for value in table.find_all('td'):
                    text = value.text
                    if text and text[0] == '.':
                        text = '0' + text

                    result.append(text.replace(',', ''))

                # 代表馬は除外
                result = result[:-1]
                results.append(result)

        return results

    def save_db(self, results):
        for data in results:
            BreederResult.objects.update_or_create(
                year=data[0],
                breeder_id=self.target_id,
                defaults={
                    'rank': data[1],
                    'first_place': data[2],
                    'second_place': data[3],
                    'third_place': data[4],
                    'unplaced': data[5],
                    'graded_runs': data[6],
                    'graded_win': data[7],
                    'special_runs': data[8],
                    'special_win': data[9],
                    'general_runs': data[10],
                    'general_win': data[11],
                    'turf_runs': data[12],
                    'turf_win': data[13],
                    'dirt_runs': data[14],
                    'dirt_win': data[15],
                    'win_rate': data[16],
                    'multiple_win_rate': data[17],
                    'show_rate': data[18],
                    'earn_prize': data[19]
                }
            )
