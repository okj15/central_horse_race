import sqlite3
import pandas as pd
import lightgbm as lgb
import optuna.integration.lightgbm as lgb_o
from sklearn.model_selection import train_test_split


class BasePredict():
    def __init__(self):
        self.db_path = '/work/data/central.db'
        self.train_sql = ''
        self.test_sql = ''
        self.test_sql_params = ()

    def read_train_data(self):
        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql_query(self.train_sql, conn)
            # 被り列削除
            df = df.loc[:, ~df.columns.duplicated()]

        # 学習データフラグ追加
        df['target'] = 0

        return df

    def read_test_data(self):
        with sqlite3.connect(self.db_path) as conn:
            if self.test_sql_params:
                df = pd.read_sql_query(self.test_sql, conn, params=self.test_sql_params)
            else:   
                df = pd.read_sql_query(self.test_sql, conn)
            # 被り列削除
            df = df.loc[:, ~df.columns.duplicated()]

        # テストデータフラグ追加
        df['target'] = 1

        return df
    
    def calc_distance_difference(self, df):
        df.loc[df['track_type_id'] == 0, 'breed_turf_dist_diff'] = df['distance'] - df['sire_turf_average_distance']
        df.loc[df['track_type_id'] == 1, 'breed_turf_dist_diff'] = df['distance'] - df['sire_dirt_average_distance']
        df.loc[df['track_type_id'] == 0, 'bms_turf_dist_diff'] = df['distance'] - df['bms_turf_average_distance']
        df.loc[df['track_type_id'] == 1, 'bms_turf_dist_diff'] = df['distance'] - df['bms_dirt_average_distance']

        return df

    def encoding_frequency(self, df, feature):
        for ft in feature:
            temp = df[ft].value_counts().to_dict()
            df[f'{ft}_count'] = df[ft].map(temp)

        return df

    def extract_field_win_rate(self, df, feature, field):
        field_dict = {
            'turf': 0,
            'dirt': 1
        }
        for fld in field:
            for ft in feature:
                df.loc[df[f'{ft}_{fld}_runs'] == 0, f'{ft}_{fld}_runs'] = 1
                df.loc[df['track_type_id'] == field_dict[fld], f'{ft}_field_rate'] = df[f'{ft}_{fld}_wins'] / df[f'{ft}_{fld}_runs']

                df.drop([f'{ft}_{fld}_runs', f'{ft}_{fld}_wins'], axis=1, inplace=True)
        
        return df

    def extract_race_win_rate(self, df, feature):
        for race_grade in ['graded', 'special', 'general']:
            for ft in feature:
                df.loc[df[f'{ft}_{race_grade}_runs'] == 0, f'{ft}_{race_grade}_runs'] = 1
                df[f'{ft}_{race_grade}_rate'] = df[f'{ft}_{race_grade}_wins'] / df[f'{ft}_{race_grade}_runs']

                df.drop([f'{ft}_{race_grade}_runs', f'{ft}_{race_grade}_wins'], axis=1, inplace=True)
        
        return df

    def convert_type(self, df):
        df = df.fillna(-999)
        df['month'] = df['month'].astype(int)
        # df['date'] = df['date'].astype(int)
        df['venue_id'] = df['venue_id'].astype('category')
        # df['race_number'] = df['race_number'].astype('category')
        df['direction_id'] = df['direction_id'].astype('category')
        df['weather_id'] = df['weather_id'].astype('category')
        df['gender_id'] = df['gender_id'].astype('category')
        df['track_condition_id'] = df['track_condition_id'].astype('category')
        df['training_center_id'] = df['training_center_id'].astype('category')
        df['starters'] = df['starters'].astype('category')
        df['bracket'] = df['bracket'].astype('category')

        return df

    def drop_data(self, df):
        
        df.drop([
            # 文字削除
            'horse_name', # 'jockey_name', 'trainer_name',
            # 固有情報削除
            'race_id', # 'horse_id', 'jockey_id', 'trainer_id',
            'race_date',
            # 'owner_id', 'father_id', 'father_father_id', 'father_mother_id',
            # 'mother_id', 'mother_father_id', 'mother_mother_id',
            # 'breed_id', 'bms_id', 'breeder_id',
            # 'birth_year', 'birth_month', 'birth_date',
            # 未来情報削除
            'race_rank',
            # 'race_time',
            # 不要そうなデータ削除
            # 'year', 'field', 'date',
            # 'odds', 'popularity',
            # 'race_number',
            'jockey_1st', 'jockey_2nd', 'jockey_3rd', 'jockey_unplaced',
            'trainer_1st', 'trainer_2nd', 'trainer_3rd', 'trainer_unplaced',
            'owner_1st', 'owner_2nd', 'owner_3rd', 'owner_unplaced',
            'breeder_1st', 'breeder_2nd', 'breeder_3rd', 'breeder_unplaced',
            # 'horse_weight', 'horse_weight_change'
        ], axis=1, inplace=True)

        return df

    def split_data(self, df):
        train_df = df[df.target == 0]
        train_df = train_df.sample(frac=1, random_state=0)
        test_df = df[df.target == 1]

        x_train_val = train_df.drop(['norm_rank', 'target'], axis=1)
        y_train_val = train_df['norm_rank']

        x_test = test_df.drop(['norm_rank', 'target'], axis=1)
        y_test = test_df['norm_rank']

        x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.3, random_state=0)

        x_train.head().to_csv('x_train.csv', index=None, encoding='utf-16')

        return x_train, x_val, x_test, y_train, y_val, y_test

    def train(self, x_train, x_val, y_train, y_val):
        lgb_train = lgb.Dataset(x_train, y_train)
        lgb_val = lgb.Dataset(x_val, y_val)

        params = {
            # 'objective': 'multiclass',
            # 'num_class': 2,
            # 'metric': 'multi_logloss',
            'metric': 'rmse',
            'verbosity': -1,
            'seed': 42,  # default: None
            # 'max_depth': 10,  # default: -1
            # 'learning_rate': 0.01,  # default: 0.1
            # 'num_leaves': 31,  # default: 31
            # 'min_data_in_leaf': 20,  # default: 20
            # 'num_iteration': 1,  # default: 100
            # 'bagging_fraction': 1.0,  # default: 1.0
            # 'bagging_freq': 1,  # default: Unknown
            # 'feature_fraction': 1.0,  # default: 1.0
        }

        gbm = lgb_o.train(
            params,
            lgb_train,
            valid_sets=[lgb_train, lgb_val],
            valid_names=['train', 'valid'],
            early_stopping_rounds=100,
            verbose_eval=1,
        )

        return gbm

    def result(self, gbm, raw_df, x_train, x_test):
        y_predict = gbm.predict(x_test)
        # accuracy = sum(y_test == np.argmax(y_predict, axis=1)) / len(y_test)
        # print('accuracy:', accuracy)
        # cm = confusion_matrix(y_test, np.argmax(y_predict, axis=1))
        # print(cm)

        result_df = pd.DataFrame({
            'race_id': raw_df[raw_df.target == 1].race_id,
            'waku': raw_df[raw_df.target == 1].bracket,
            'horse_number': raw_df[raw_df.target == 1].horse_number,
            'horse_name': raw_df[raw_df.target == 1].horse_name,
            'predict': y_predict,
            # 'odds': raw_df[raw_df.target == 1].odds
        })

        x_test.to_csv('x_test.csv', index=None, encoding='utf-16')
        result_df.to_csv('res.csv', index=None, encoding='utf-16')

        for i, res in result_df.groupby('race_id'):
            print(res.sort_values('predict'))
            print()

        # 頻度
        frequency = pd.DataFrame(gbm.feature_importance(importance_type='split'), index=x_train.columns,
                                columns=['importance'])
        frequency = frequency.sort_values('importance', ascending=False)
        print(frequency)

        # ゲイン
        gain = pd.DataFrame(gbm.feature_importance(importance_type='gain'), index=x_train.columns,
                            columns=['importance'])
        gain = gain.sort_values('importance', ascending=False)
        print(gain)