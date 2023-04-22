from base import BasePredict
import pandas as pd


class SinbaPredict(BasePredict):

    def __init__(self):
        super().__init__()
        self.train_sql = '''
            SELECT 
                race_id, result_race.rank as race_rank, strftime('%Y-%m-%d', race_date) as race_date, strftime('%m', race_date) as month,
                basic_info_horse.name as horse_name,
                venue_id, race_class, distance, track_type_id, track_condition_id, direction_id, weather_id, starters, bracket, horse_number, gender_id, age, jockey_weight, training_center_id,
                result_jockey.rank as jockey_rank,
                result_jockey.first as jockey_1st,
                result_jockey.second as jockey_2nd, 
                result_jockey.third as jockey_3rd,
                result_jockey.unplaced as jockey_unplaced,
                result_jockey.graded_runs as jockey_graded_runs,
                result_jockey.graded_wins as jockey_graded_wins,
                result_jockey.special_runs as jockey_special_runs,
                result_jockey.special_wins as jockey_special_wins,
                result_jockey.general_runs as jockey_general_runs,
                result_jockey.general_wins as jockey_general_wins,
                result_jockey.turf_runs as jockey_turf_runs,
                result_jockey.turf_wins as jockey_turf_wins,
                result_jockey.dirt_runs as jockey_dirt_runs,
                result_jockey.dirt_wins as jockey_dirt_wins,
                result_jockey.win_rate as jockey_win_rate,
                result_jockey.quinella_rate as jockey_quinella_rate,
                result_jockey.show_rate as jockey_show_rate,
                result_jockey.earnings as jockey_earnings,
                result_trainer.rank as trainer_rank,
                result_trainer.first as trainer_1st,
                result_trainer.second as trainer_2nd, 
                result_trainer.third as trainer_3rd,
                result_trainer.unplaced as trainer_unplaced,
                result_trainer.graded_runs as trainer_graded_runs,
                result_trainer.graded_wins as trainer_graded_wins,
                result_trainer.special_runs as trainer_special_runs,
                result_trainer.special_wins as trainer_special_wins,
                result_trainer.general_runs as trainer_general_runs,
                result_trainer.general_wins as trainer_general_wins,
                result_trainer.turf_runs as trainer_turf_runs,
                result_trainer.turf_wins as trainer_turf_wins,
                result_trainer.dirt_runs as trainer_dirt_runs,
                result_trainer.dirt_wins as trainer_dirt_wins,
                result_trainer.win_rate as trainer_win_rate,
                result_trainer.quinella_rate as trainer_quinella_rate,
                result_trainer.show_rate as trainer_show_rate,
                result_trainer.earnings as trainer_earnings,
                result_owner.rank as owner_rank,
                result_owner.first as owner_1st,
                result_owner.second as owner_2nd, 
                result_owner.third as owner_3rd,
                result_owner.unplaced as owner_unplaced,
                result_owner.graded_runs as owner_graded_runs,
                result_owner.graded_wins as owner_graded_wins,
                result_owner.special_runs as owner_special_runs,
                result_owner.special_wins as owner_special_wins,
                result_owner.general_runs as owner_general_runs,
                result_owner.general_wins as owner_general_wins,
                result_owner.turf_runs as owner_turf_runs,
                result_owner.turf_wins as owner_turf_wins,
                result_owner.dirt_runs as owner_dirt_runs,
                result_owner.dirt_wins as owner_dirt_wins,
                result_owner.win_rate as owner_win_rate,
                result_owner.quinella_rate as owner_quinella_rate,
                result_owner.show_rate as owner_show_rate,
                result_owner.earnings as owner_earnings,
                result_breeder.rank as breeder_rank,
                result_breeder.first as breeder_1st,
                result_breeder.second as breeder_2nd, 
                result_breeder.third as breeder_3rd,
                result_breeder.unplaced as breeder_unplaced,
                result_breeder.graded_runs as breeder_graded_runs,
                result_breeder.graded_wins as breeder_graded_wins,
                result_breeder.special_runs as breeder_special_runs,
                result_breeder.special_wins as breeder_special_wins,
                result_breeder.general_runs as breeder_general_runs,
                result_breeder.general_wins as breeder_general_wins,
                result_breeder.turf_runs as breeder_turf_runs,
                result_breeder.turf_wins as breeder_turf_wins,
                result_breeder.dirt_runs as breeder_dirt_runs,
                result_breeder.dirt_wins as breeder_dirt_wins,
                result_breeder.win_rate as breeder_win_rate,
                result_breeder.quinella_rate as breeder_quinella_rate,
                result_breeder.show_rate as breeder_show_rate,
                result_breeder.earnings as breeder_earnings,
                result_sire.rank as sire_rank,
                result_sire.foals as sire_foals,
                result_sire.winners as sire_winners,
                result_sire.wins as sire_wins,
                result_sire.graded_runs as sire_graded_runs,
                result_sire.graded_wins as sire_graded_wins,
                result_sire.special_runs as sire_special_runs,
                result_sire.special_wins as sire_special_wins,
                result_sire.general_runs as sire_general_runs,
                result_sire.general_wins as sire_general_wins,
                result_sire.turf_runs as sire_turf_runs,
                result_sire.turf_wins as sire_turf_wins,
                result_sire.dirt_runs as sire_dirt_runs,
                result_sire.dirt_wins as sire_dirt_wins,
                result_sire.win_rate as sire_win_rate,
                result_sire.ei as sire_ei,
                result_sire.earnings as sire_earnings,
                result_sire.turf_average_distance as sire_turf_average_distance,
                result_sire.dirt_average_distance as sire_dirt_average_distance,
                result_bms.rank as bms_rank,
                result_bms.foals as bms_foals,
                result_bms.winners as bms_winners,
                result_bms.wins as bms_wins,
                result_bms.graded_runs as bms_graded_runs,
                result_bms.graded_wins as bms_graded_wins,
                result_bms.special_runs as bms_special_runs,
                result_bms.special_wins as bms_special_wins,
                result_bms.general_runs as bms_general_runs,
                result_bms.general_wins as bms_general_wins,
                result_bms.turf_runs as bms_turf_runs,
                result_bms.turf_wins as bms_turf_wins,
                result_bms.dirt_runs as bms_dirt_runs,
                result_bms.dirt_wins as bms_dirt_wins,
                result_bms.win_rate as bms_win_rate,
                result_bms.ei as bms_ei,
                result_bms.earnings as bms_earnings,
                result_bms.turf_average_distance as bms_turf_average_distance,
                result_bms.dirt_average_distance as bms_dirt_average_distance
            FROM result_race
                LEFT JOIN basic_info_horse
                ON
                    result_race.horse_id = basic_info_horse.id
                LEFT JOIN result_jockey
                ON
                    result_race.jockey_id = result_jockey.jockey_id AND
                    strftime('%Y', result_race.race_date) - 1 = result_jockey.year
                LEFT JOIN result_trainer
                ON
                    result_race.trainer_id = result_trainer.trainer_id AND
                    strftime('%Y', result_race.race_date) - 1 = result_trainer.year
                LEFT JOIN result_owner
                ON
                    basic_info_horse.owner_id = result_owner.owner_id AND
                    strftime('%Y', result_race.race_date) - 1 = result_owner.year
                LEFT JOIN result_breeder
                ON
                    basic_info_horse.breeder_id = result_breeder.breeder_id AND
                    strftime('%Y', result_race.race_date) - 1 = result_breeder.year
                LEFT JOIN result_sire
                ON
                    basic_info_horse.father_id = result_sire.sire_id AND
                    strftime('%Y', result_race.race_date) - 1 = result_sire.year
                LEFT JOIN result_bms
                ON
                    basic_info_horse.mother_father_id = result_bms.bms_id AND
                    strftime('%Y', result_race.race_date) - 1 = result_bms.year
            WHERE
                result_race.race_class = 700;
        '''

    def extract_feature(self, df):
        # 頻度エンコード
        # df = self.encoding_frequency(df, feature=['age', 'venue_id', 'gender_id', 'track_condition_id', 'starters', 'bracket'])

        # 最終出力用にコピー
        raw_df = df.copy()

        # 産駒平均距離と対象レースとの差
        df = self.calc_distance_difference(df)

        # 馬場別勝率
        df = self.extract_field_win_rate(df, feature=['jockey', 'trainer', 'owner', 'sire', 'bms'],
                                         field=['turf', 'dirt'])

        # レースごと勝率
        df = self.extract_race_win_rate(df, feature=['jockey', 'trainer', 'owner'])

        # 教師ラベル付与
        df['norm_rank'] = df['race_rank'] / df.starters

        # タイプ変換
        df = self.convert_type(df)

        # 不要データ削除
        df = self.drop_data(df)

        return df, raw_df


def main():
    target_date = '2021-08-21'
    sinba_predict = SinbaPredict()
    df = sinba_predict.read_train_data()
    train_df = df[(df.race_date != target_date) & (df.race_rank.notna())]
    test_df = df[df.race_date == target_date]
    test_df.target = 1

    # test_df = sinba_predict.read_test_data()

    # 頻度エンコード出すためにいったん結合
    df = pd.concat([train_df, test_df], axis=0, ignore_index=True)
    df, raw_df = sinba_predict.extract_feature(df)

    # 学習データ, テストデータに再分割
    x_train, x_val, x_test, y_train, y_val, y_test = sinba_predict.split_data(df)

    # 学習
    gbm = sinba_predict.train(x_train, x_val, y_train, y_val)

    sinba_predict.result(gbm, raw_df, x_train, x_test)


if __name__ == '__main__':
    main()
