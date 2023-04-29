from django.core.management.base import BaseCommand

from result.models import Race


class Command(BaseCommand):
    def handle(self, *args, **options):
        race = Race.objects.filter(horse__father == '2003102205')
