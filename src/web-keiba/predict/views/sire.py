from result.models import Race

def get_sire_result(target_race):

    # 通算成績
    sire_total_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(rank__isnull=False, horse__father=target.horse.father).values_list('rank', flat=True))
        sire_total_results[target.horse] =  convert_record(record, target)

    # コース勝率
    sire_venue_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(venue__name=target.venue, rank__isnull=False, horse__father=target.horse.father).values_list('rank', flat=True))
        sire_venue_results[target.horse] =  convert_record(record, target)

    # 枠勝率
    sire_bracket_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(bracket=target.bracket, rank__isnull=False, horse__father=target.horse.father).values_list('rank', flat=True))
        sire_bracket_results[target.horse] =  convert_record(record, target)

    # コース * 枠勝率
    sire_venue_bracket_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(venue__name=target.venue, bracket=target.bracket, rank__isnull=False, horse__father=target.horse.father).values_list('rank', flat=True))
        sire_venue_bracket_results[target.horse] =  convert_record(record, target)

    # 馬場状態勝率
    sire_condition_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(track_condition__name=target.track_condition, rank__isnull=False, horse__father=target.horse.father).values_list('rank', flat=True))
        sire_condition_results[target.horse] =  convert_record(record, target)

    # 回り勝率
    sire_direction_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(direction__name=target.direction, rank__isnull=False, horse__father=target.horse.father).values_list('rank', flat=True))
        sire_direction_results[target.horse] =  convert_record(record, target)


    return {
        '通算': sire_total_results,
        '開催地': sire_venue_results,
        '枠': sire_bracket_results,
        '開催地×枠': sire_venue_bracket_results,
        '馬場状態': sire_condition_results,
        '回り': sire_direction_results
    }

def convert_record(record, target):
    under_4 = len(record) - (record.count(1) + record.count(2) + record.count(3))
    if len(record) == 0:
        record = [0]
    return [
            target.horse.father,
            f'{record.count(1)} ({round(record.count(1) * 100 / len(record), 2)}%)',
            f'{record.count(2)} ({round(record.count(2) * 100 / len(record), 2)}%)',
            f'{record.count(3)} ({round(record.count(3) * 100 / len(record), 2)}%)',
            f'{under_4} ({round(under_4 * 100 / len(record), 2)}%)',
        ]