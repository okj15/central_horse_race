from django.core.management.base import BaseCommand
from django.conf import settings

from result.models import Race

import pandas as pd

class Command(BaseCommand):
    def handle(self, *args, **options):
        race = Race.objects.filter(horse__father=='2003102205')