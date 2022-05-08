import sqlite3
import pandas as pd

"""
血統情報による分析
"""

db_path = 'data/keiba.db'
race_id = '202105030105'

def get_race_data():
    sql = '''
        SELECT *
        FROM t_race_realtime
            LEFT JOIN t_horse_base
            ON
                t_race_realtime.horse_id = t_horse_base.horse_id
        WHERE
            race_id = ?;
    '''
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(sql, conn, params=(race_id, ))
    
    return df


def get_breed_data(horse_names, breed_ids):
    sql = '''
        SELECT *
        FROM t_breed
        WHERE
            breed_id = ?;
    '''
    with sqlite3.connect(db_path) as conn:
        for horse_name, breed_id in zip(horse_names, breed_ids):
            df = pd.read_sql_query(sql, conn, params=(breed_id, ))
            print(horse_name, df.breed_turf_race_win.iloc[0], df.breed_win_rate.iloc[0])

    return df

def get_bms_data(horse_names, breed_ids):
    sql = '''
        SELECT *
        FROM t_bms
        WHERE
            bms_id = ?;
    '''
    with sqlite3.connect(db_path) as conn:
        for horse_name, breed_id in zip(horse_names, breed_ids):
            df = pd.read_sql_query(sql, conn, params=(breed_id, ))
            print(horse_name, df.breed_turf_race_win.iloc[0], df.breed_win_rate.iloc[0])

    return df

def main():
    # 該当レースの取得
    race_df = get_race_data()
    horse_names = list(race_df.horse_name)
    breed_ids = list(race_df.father_id)
    bms_ids = list(race_df.mother_father_id)

    # breed情報取得
    get_breed_data(horse_names, breed_ids)

    print()

    # bms情報取得
    get_breed_data(horse_names, bms_ids)

if __name__ == '__main__':
    main()