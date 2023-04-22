import collections
from django.db.models import base

from django.shortcuts import render
from result.models import Race
from basic_info.models import Jockey


def index(request, *args, **kwargs):
    base_race_id = int(request.GET['id']) * 100
    venue = str(base_race_id)[4:6]

    results = []
    for i in range(1, 13):
        result = dict()

        race = Race.objects.filter(race_id=base_race_id + i).all()
        target_jockey = list(race.values_list('jockey', flat=True))
        track_type = race.first().track_type

        venue_result = Race.objects.filter(jockey__in=target_jockey, venue=venue, track_type__name=track_type,
                                           race_date__year=2021)
        venue_jockey = set(venue_result.values_list('jockey', flat=True))
        venue_win = collections.Counter(venue_result.filter(rank=1).values_list('jockey', flat=True))
        venue_show = collections.Counter(venue_result.filter(rank__lte=3).values_list('jockey', flat=True))

        jockey_venue_wins = dict()
        jockey_venue_shows = dict()
        for jockey in venue_jockey:
            races = len(venue_result.filter(jockey=jockey))
            j = Jockey.objects.filter(id=jockey).first()
            jockey_venue_wins[j] = round(venue_win[jockey] / races, 2)
            jockey_venue_shows[j] = round(venue_show[jockey] / races, 2)

        result['開催地勝率'] = dict(sorted(jockey_venue_wins.items(), key=lambda x: x[1], reverse=True))
        result['開催地複勝率'] = dict(sorted(jockey_venue_shows.items(), key=lambda x: x[1], reverse=True))

        results.append(result)

    context = {
        'results': results
    }

    return render(request, 'predict/matome.html', context=context)
