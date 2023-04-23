# Generated by Django 3.2.5 on 2021-08-06 11:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('result', '0001_squashed_0008_auto_20210806_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jockey',
            old_name='dirt_race',
            new_name='dirt_runs',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='dirt_race_win',
            new_name='dirt_wins',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='get_prize',
            new_name='earnings',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='general_race',
            new_name='general_runs',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='general_race_win',
            new_name='general_wins',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='graded_race',
            new_name='graded_runs',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='graded_race_win',
            new_name='graded_wins',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='special_race',
            new_name='special_runs',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='special_race_win',
            new_name='special_wins',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='turf_race',
            new_name='turf_runs',
        ),
        migrations.RenameField(
            model_name='jockey',
            old_name='turf_race_win',
            new_name='turf_wins',
        ),
    ]
