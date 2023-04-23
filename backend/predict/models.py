# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bms(models.Model):
    bms_id = models.TextField(blank=True, null=True)
    bms_rank = models.IntegerField(blank=True, null=True)
    bms_horse_num = models.IntegerField(blank=True, null=True)
    bms_horse_win_num = models.IntegerField(blank=True, null=True)
    bms_race_num = models.IntegerField(blank=True, null=True)
    bms_race_win_num = models.IntegerField(blank=True, null=True)
    bms_graded_race = models.IntegerField(blank=True, null=True)
    bms_graded_race_win = models.IntegerField(blank=True, null=True)
    bms_special_race = models.IntegerField(blank=True, null=True)
    bms_special_race_win = models.IntegerField(blank=True, null=True)
    bms_general_race = models.IntegerField(blank=True, null=True)
    bms_general_race_win = models.IntegerField(blank=True, null=True)
    bms_turf_race = models.IntegerField(blank=True, null=True)
    bms_turf_race_win = models.IntegerField(blank=True, null=True)
    bms_dirt_race = models.IntegerField(blank=True, null=True)
    bms_dirt_race_win = models.IntegerField(blank=True, null=True)
    bms_win_rate = models.FloatField(blank=True, null=True)
    bms_ei = models.FloatField(blank=True, null=True)
    bms_get_prize = models.FloatField(blank=True, null=True)
    bms_average_turf_dist = models.FloatField(blank=True, null=True)
    bms_average_dirt_dist = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bms'


class Breed(models.Model):
    breed_id = models.TextField(blank=True, null=True)
    breed_rank = models.IntegerField(blank=True, null=True)
    breed_horse_num = models.IntegerField(blank=True, null=True)
    breed_horse_win_num = models.IntegerField(blank=True, null=True)
    breed_race_num = models.IntegerField(blank=True, null=True)
    breed_race_win_num = models.IntegerField(blank=True, null=True)
    breed_graded_race = models.IntegerField(blank=True, null=True)
    breed_graded_race_win = models.IntegerField(blank=True, null=True)
    breed_special_race = models.IntegerField(blank=True, null=True)
    breed_special_race_win = models.IntegerField(blank=True, null=True)
    breed_general_race = models.IntegerField(blank=True, null=True)
    breed_general_race_win = models.IntegerField(blank=True, null=True)
    breed_turf_race = models.IntegerField(blank=True, null=True)
    breed_turf_race_win = models.IntegerField(blank=True, null=True)
    breed_dirt_race = models.IntegerField(blank=True, null=True)
    breed_dirt_race_win = models.IntegerField(blank=True, null=True)
    breed_win_rate = models.FloatField(blank=True, null=True)
    breed_ei = models.FloatField(blank=True, null=True)
    breed_get_prize = models.FloatField(blank=True, null=True)
    breed_average_turf_dist = models.FloatField(blank=True, null=True)
    breed_average_dirt_dist = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'breed'


class HorseBase(models.Model):
    horse_base = models.TextField(db_column='horse_id', unique=True, blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True)
    birth_month = models.IntegerField(blank=True, null=True)
    birth_date = models.IntegerField(blank=True, null=True)
    owner_id = models.TextField(blank=True, null=True)
    breeder_id = models.TextField(blank=True, null=True)
    father_id = models.TextField(db_column='father_id', blank=True, null=True)
    father_father_id = models.TextField(db_column='father_father_id', blank=True, null=True)
    father_mother_id = models.TextField(blank=True, null=True)
    mother_id = models.TextField(blank=True, null=True)
    mother_father_id = models.TextField(blank=True, null=True)
    mother_mother_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horse_base'


class HorseRace(models.Model):
    horse_base = models.ForeignKey(HorseBase, db_column='horse_id', to_field='horse_base', on_delete=models.CASCADE)
    race_id = models.IntegerField(blank=True, null=True)
    race_name = models.TextField(blank=True, null=True)
    race_date = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    horse_weather = models.IntegerField(blank=True, null=True)
    horse_race_number = models.IntegerField(blank=True, null=True)
    starters_number = models.IntegerField(blank=True, null=True)
    waku = models.IntegerField(blank=True, null=True)
    horse_number = models.IntegerField(blank=True, null=True)
    odds = models.FloatField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    jockey_id = models.TextField(blank=True, null=True)
    jockey_weight = models.FloatField(blank=True, null=True)
    field = models.IntegerField(blank=True, null=True)
    dist = models.IntegerField(blank=True, null=True)
    field_condition = models.IntegerField(blank=True, null=True)
    race_time = models.FloatField(blank=True, null=True)
    diff = models.FloatField(blank=True, null=True)
    corner_rank_1st = models.IntegerField(blank=True, null=True)
    corner_rank_2nd = models.IntegerField(blank=True, null=True)
    corner_rank_3rd = models.IntegerField(blank=True, null=True)
    corner_rank_4th = models.IntegerField(blank=True, null=True)
    pace1 = models.FloatField(blank=True, null=True)
    pace2 = models.FloatField(blank=True, null=True)
    three_halon = models.FloatField(blank=True, null=True)
    horse_weight = models.IntegerField(blank=True, null=True)
    horse_weight_change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horse_race'


class Jockey(models.Model):
    jockey_id = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    jockey_year_rank = models.IntegerField(blank=True, null=True)
    jockey_year_1st = models.IntegerField(blank=True, null=True)
    jockey_year_2nd = models.IntegerField(blank=True, null=True)
    jockey_year_3rd = models.IntegerField(blank=True, null=True)
    jockey_year_4th = models.IntegerField(blank=True, null=True)
    jockey_year_graded_race = models.IntegerField(blank=True, null=True)
    jockey_year_graded_race_win = models.IntegerField(blank=True, null=True)
    jockey_year_special_race = models.IntegerField(blank=True, null=True)
    jockey_year_special_race_win = models.IntegerField(blank=True, null=True)
    jockey_year_general_race = models.IntegerField(blank=True, null=True)
    jockey_year_general_race_win = models.IntegerField(blank=True, null=True)
    jockey_year_turf_race = models.IntegerField(blank=True, null=True)
    jockey_year_turf_race_win = models.IntegerField(blank=True, null=True)
    jockey_year_dirt_race = models.IntegerField(blank=True, null=True)
    jockey_year_dirt_race_win = models.IntegerField(blank=True, null=True)
    jockey_year_win_rate = models.FloatField(blank=True, null=True)
    jockey_year_1st_or_2nd_rate = models.FloatField(blank=True, null=True)
    jockey_year_show_rate = models.FloatField(blank=True, null=True)
    jockey_year_get_prize = models.FloatField(blank=True, null=True)
    jockey_total_1st = models.IntegerField(blank=True, null=True)
    jockey_total_2nd = models.IntegerField(blank=True, null=True)
    jockey_total_3rd = models.IntegerField(blank=True, null=True)
    jockey_total_4th = models.IntegerField(blank=True, null=True)
    jockey_total_graded_race = models.IntegerField(blank=True, null=True)
    jockey_total_graded_race_win = models.IntegerField(blank=True, null=True)
    jockey_total_special_race = models.IntegerField(blank=True, null=True)
    jockey_total_special_race_win = models.IntegerField(blank=True, null=True)
    jockey_total_general_race = models.IntegerField(blank=True, null=True)
    jockey_total_general_race_win = models.IntegerField(blank=True, null=True)
    jockey_total_turf_race = models.IntegerField(blank=True, null=True)
    jockey_total_turf_race_win = models.IntegerField(blank=True, null=True)
    jockey_total_dirt_race = models.IntegerField(blank=True, null=True)
    jockey_total_dirt_race_win = models.IntegerField(blank=True, null=True)
    jockey_total_win_rate = models.FloatField(blank=True, null=True)
    jockey_total_1st_or_2nd_rate = models.FloatField(blank=True, null=True)
    jockey_total_show_rate = models.FloatField(blank=True, null=True)
    jockey_total_get_prize = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jockey'


class Owner(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    owner_year_rank = models.IntegerField(blank=True, null=True)
    owner_year_1st = models.IntegerField(blank=True, null=True)
    owner_year_2nd = models.IntegerField(blank=True, null=True)
    owner_year_3rd = models.IntegerField(blank=True, null=True)
    owner_year_4th = models.IntegerField(blank=True, null=True)
    owner_year_graded_race = models.IntegerField(blank=True, null=True)
    owner_year_graded_race_win = models.IntegerField(blank=True, null=True)
    owner_year_special_race = models.IntegerField(blank=True, null=True)
    owner_year_special_race_win = models.IntegerField(blank=True, null=True)
    owner_year_general_race = models.IntegerField(blank=True, null=True)
    owner_year_general_race_win = models.IntegerField(blank=True, null=True)
    owner_year_turf_race = models.IntegerField(blank=True, null=True)
    owner_year_turf_race_win = models.IntegerField(blank=True, null=True)
    owner_year_dirt_race = models.IntegerField(blank=True, null=True)
    owner_year_dirt_race_win = models.IntegerField(blank=True, null=True)
    owner_year_win_rate = models.FloatField(blank=True, null=True)
    owner_year_1st_or_2nd_rate = models.FloatField(blank=True, null=True)
    owner_year_show_rate = models.FloatField(blank=True, null=True)
    owner_year_get_prize = models.FloatField(blank=True, null=True)
    owner_total_1st = models.IntegerField(blank=True, null=True)
    owner_total_2nd = models.IntegerField(blank=True, null=True)
    owner_total_3rd = models.IntegerField(blank=True, null=True)
    owner_total_4th = models.IntegerField(blank=True, null=True)
    owner_total_graded_race = models.IntegerField(blank=True, null=True)
    owner_total_graded_race_win = models.IntegerField(blank=True, null=True)
    owner_total_special_race = models.IntegerField(blank=True, null=True)
    owner_total_special_race_win = models.IntegerField(blank=True, null=True)
    owner_total_general_race = models.IntegerField(blank=True, null=True)
    owner_total_general_race_win = models.IntegerField(blank=True, null=True)
    owner_total_turf_race = models.IntegerField(blank=True, null=True)
    owner_total_turf_race_win = models.IntegerField(blank=True, null=True)
    owner_total_dirt_race = models.IntegerField(blank=True, null=True)
    owner_total_dirt_race_win = models.IntegerField(blank=True, null=True)
    owner_total_win_rate = models.FloatField(blank=True, null=True)
    owner_total_1st_or_2nd_rate = models.FloatField(blank=True, null=True)
    owner_total_show_rate = models.FloatField(blank=True, null=True)
    owner_total_get_prize = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'owner'


class Race(models.Model):
    race_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    race_class = models.IntegerField(blank=True, null=True)
    race_number = models.IntegerField(blank=True, null=True)
    field = models.IntegerField(blank=True, null=True)
    dist = models.IntegerField(blank=True, null=True)
    field_condition = models.IntegerField(blank=True, null=True)
    l_or_r = models.IntegerField(blank=True, null=True)
    weather = models.IntegerField(blank=True, null=True)
    starters_number = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    waku = models.IntegerField(blank=True, null=True)
    horse_number = models.IntegerField(blank=True, null=True)
    horse_id = models.IntegerField(blank=True, null=True)
    horse_name = models.TextField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    jockey_weight = models.FloatField(blank=True, null=True)
    jockey_id = models.TextField(blank=True, null=True)
    jockey_name = models.TextField(blank=True, null=True)
    race_time = models.FloatField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    odds = models.FloatField(blank=True, null=True)
    three_halon = models.FloatField(blank=True, null=True)
    corner_rank_1st = models.IntegerField(blank=True, null=True)
    corner_rank_2nd = models.IntegerField(blank=True, null=True)
    corner_rank_3rd = models.IntegerField(blank=True, null=True)
    corner_rank_4th = models.IntegerField(blank=True, null=True)
    training_center = models.IntegerField(blank=True, null=True)
    trainer_id = models.TextField(blank=True, null=True)
    trainer_name = models.TextField(blank=True, null=True)
    horse_weight = models.IntegerField(blank=True, null=True)
    horse_weight_change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'race'


class RaceRealtime(models.Model):
    race_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    race_class = models.IntegerField(blank=True, null=True)
    race_number = models.IntegerField(blank=True, null=True)
    field = models.IntegerField(blank=True, null=True)
    dist = models.IntegerField(blank=True, null=True)
    field_condition = models.IntegerField(blank=True, null=True)
    l_or_r = models.IntegerField(blank=True, null=True)
    weather = models.IntegerField(blank=True, null=True)
    starters_number = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    waku = models.IntegerField(blank=True, null=True)
    horse_number = models.IntegerField(blank=True, null=True)
    horse_id = models.TextField(blank=True, null=True)
    horse_name = models.TextField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    jockey_weight = models.FloatField(blank=True, null=True)
    jockey_id = models.TextField(blank=True, null=True)
    jockey_name = models.TextField(blank=True, null=True)
    race_time = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    odds = models.FloatField(blank=True, null=True)
    training_center = models.IntegerField(blank=True, null=True)
    trainer_id = models.TextField(blank=True, null=True)
    trainer_name = models.TextField(blank=True, null=True)
    horse_weight = models.IntegerField(blank=True, null=True)
    horse_weight_change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'race_realtime'


class Trainer(models.Model):
    trainer_id = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    trainer_year_rank = models.IntegerField(blank=True, null=True)
    trainer_year_1st = models.IntegerField(blank=True, null=True)
    trainer_year_2nd = models.IntegerField(blank=True, null=True)
    trainer_year_3rd = models.IntegerField(blank=True, null=True)
    trainer_year_4th = models.IntegerField(blank=True, null=True)
    trainer_year_graded_race = models.IntegerField(blank=True, null=True)
    trainer_year_graded_race_win = models.IntegerField(blank=True, null=True)
    trainer_year_special_race = models.IntegerField(blank=True, null=True)
    trainer_year_special_race_win = models.IntegerField(blank=True, null=True)
    trainer_year_general_race = models.IntegerField(blank=True, null=True)
    trainer_year_general_race_win = models.IntegerField(blank=True, null=True)
    trainer_year_turf_race = models.IntegerField(blank=True, null=True)
    trainer_year_turf_race_win = models.IntegerField(blank=True, null=True)
    trainer_year_dirt_race = models.IntegerField(blank=True, null=True)
    trainer_year_dirt_race_win = models.IntegerField(blank=True, null=True)
    trainer_year_win_rate = models.FloatField(blank=True, null=True)
    trainer_year_1st_or_2nd_rate = models.FloatField(blank=True, null=True)
    trainer_year_show_rate = models.FloatField(blank=True, null=True)
    trainer_year_get_prize = models.FloatField(blank=True, null=True)
    trainer_total_1st = models.IntegerField(blank=True, null=True)
    trainer_total_2nd = models.IntegerField(blank=True, null=True)
    trainer_total_3rd = models.IntegerField(blank=True, null=True)
    trainer_total_4th = models.IntegerField(blank=True, null=True)
    trainer_total_graded_race = models.IntegerField(blank=True, null=True)
    trainer_total_graded_race_win = models.IntegerField(blank=True, null=True)
    trainer_total_special_race = models.IntegerField(blank=True, null=True)
    trainer_total_special_race_win = models.IntegerField(blank=True, null=True)
    trainer_total_general_race = models.IntegerField(blank=True, null=True)
    trainer_total_general_race_win = models.IntegerField(blank=True, null=True)
    trainer_total_turf_race = models.IntegerField(blank=True, null=True)
    trainer_total_turf_race_win = models.IntegerField(blank=True, null=True)
    trainer_total_dirt_race = models.IntegerField(blank=True, null=True)
    trainer_total_dirt_race_win = models.IntegerField(blank=True, null=True)
    trainer_total_win_rate = models.FloatField(blank=True, null=True)
    trainer_total_1st_or_2nd_rate = models.FloatField(blank=True, null=True)
    trainer_total_show_rate = models.FloatField(blank=True, null=True)
    trainer_total_get_prize = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainer'
