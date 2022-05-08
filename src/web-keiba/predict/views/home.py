import collections

from django.shortcuts import render
from result.models import Race
from .jockey import get_jockey_result
from .horse import get_horse_result
from .sire import get_sire_result

def index(request, *args, **kwargs):

    # レース情報取得
    target_race = Race.objects.filter(race_id=request.GET['id']).order_by('race_id', 'horse_number')

    jockey_results = get_jockey_result(target_race)
    horse_results = get_horse_result(target_race)
    sire_results = get_sire_result(target_race)

    context = {
        'target_race': target_race,
        'jockey_results': jockey_results,
        'horse_results': horse_results,
        'sire_results': sire_results
    }

    return render(request, 'predict/index.html', context=context)
