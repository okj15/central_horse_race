from result.models import Race


def get_jockey_result(target_race):
    # コース勝率
    jockey_venue_results = dict()
    for target in target_race:
        record = list(
            Race.objects.filter(venue__name=target.venue, rank__isnull=False, jockey=target.jockey).values_list('rank',
                                                                                                                flat=True))
        jockey_venue_results[target.horse] = convert_record(record, target)

    # 枠勝率
    jockey_bracket_results = dict()
    for target in target_race:
        record = list(
            Race.objects.filter(bracket=target.bracket, rank__isnull=False, jockey=target.jockey).values_list('rank',
                                                                                                              flat=True))
        jockey_bracket_results[target.horse] = convert_record(record, target)

    # コース * 枠勝率
    jockey_venue_bracket_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(venue__name=target.venue, bracket=target.bracket, rank__isnull=False,
                                          jockey=target.jockey).values_list('rank', flat=True))
        jockey_venue_bracket_results[target.horse] = convert_record(record, target)

    # 馬場状態勝率
    jockey_condition_results = dict()
    for target in target_race:
        record = list(Race.objects.filter(track_condition__name=target.track_condition, rank__isnull=False,
                                          jockey=target.jockey).values_list('rank', flat=True))
        jockey_condition_results[target.horse] = convert_record(record, target)

    return {
        '開催地': jockey_venue_results,
        '枠': jockey_bracket_results,
        '開催地×枠': jockey_venue_bracket_results,
        '馬場状態': jockey_condition_results,
    }


def convert_record(record, target):
    under_4 = len(record) - (record.count(1) + record.count(2) + record.count(3))
    if len(record) == 0:
        record = [0]
    return [
        target.jockey,
        f'{record.count(1)} ({round(record.count(1) * 100 / len(record), 2)}%)',
        f'{record.count(2)} ({round(record.count(2) * 100 / len(record), 2)}%)',
        f'{record.count(3)} ({round(record.count(3) * 100 / len(record), 2)}%)',
        f'{under_4} ({round(under_4 * 100 / len(record), 2)}%)',
    ]
