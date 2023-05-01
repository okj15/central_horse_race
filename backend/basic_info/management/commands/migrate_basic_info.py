
from django.core.management.base import BaseCommand

from ...models import Jockey
from jockey.models import Master


class Command(BaseCommand):

    def handle(self, *args, **options):
        # basic_infoのデータを新しいappに移行する
        for old_data in Jockey.objects.all().order_by('id'):
            Master.objects.create(
                id=old_data.id,
                name=old_data.name
            )
            print(old_data.id, old_data.name)
