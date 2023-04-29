from result.models import Race


def get_horse_result(target_race):
    # 通算成績
    horse_total_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(rank__isnull=False, horse=target.horse).values_list('rank', flat=True))
        horse_total_results[target.horse] = convert_record(record)

    # コース勝率
    horse_venue_results = dict()
    for target in target_race:
        record = list(
            Race.objects.filter(venue__name=target.venue, rank__isnull=False, horse=target.horse).values_list('rank',
                                                                                                              flat=True))
        horse_venue_results[target.horse] = convert_record(record)

    # 枠勝率
    horse_bracket_results = dict()
    for target in target_race:
        record = list(
            Race.objects.filter(bracket=target.bracket, rank__isnull=False, horse=target.horse).values_list('rank',
                                                                                                            flat=True))
        horse_bracket_results[target.horse] = convert_record(record)

    # コース * 枠勝率
    horse_venue_bracket_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(venue__name=target.venue, bracket=target.bracket, rank__isnull=False,
                                          horse=target.horse).values_list('rank', flat=True))
        horse_venue_bracket_results[target.horse] = convert_record(record)

    # 馬場状態勝率
    horse_condition_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(track_condition__name=target.track_condition, rank__isnull=False,
                                          horse=target.horse).values_list('rank', flat=True))
        horse_condition_results[target.horse] = convert_record(record)

    # 回り勝率
    horse_direction_results = dict()
    for target in target_race:
        record = list(
            Race.objects.filter(direction__name=target.direction, rank__isnull=False, horse=target.horse).values_list(
                'rank', flat=True))
        horse_direction_results[target.horse] = convert_record(record)

    return {
        '通算': horse_total_results,
        '開催地': horse_venue_results,
        '枠': horse_bracket_results,
        '開催地×枠': horse_venue_bracket_results,
        '馬場状態': horse_condition_results,
        '回り': horse_direction_results
    }


def convert_record(record):
    under_4 = len(record) - (record.count(1) + record.count(2) + record.count(3))
    if len(record) == 0:
        record = [0]
    return [
        f'{record.count(1)} ({round(record.count(1) * 100 / len(record), 2)}%)',
        f'{record.count(2)} ({round(record.count(2) * 100 / len(record), 2)}%)',
        f'{record.count(3)} ({round(record.count(3) * 100 / len(record), 2)}%)',
        f'{under_4} ({round(under_4 * 100 / len(record), 2)}%)',
    ]
