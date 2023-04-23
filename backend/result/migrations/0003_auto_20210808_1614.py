# Generated by Django 3.2.5 on 2021-08-08 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('race_info', '0003_auto_20210801_1004'),
        ('basic_info', '0005_auto_20210804_1629'),
        ('result', '0002_auto_20210806_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_id', models.IntegerField()),
                ('race_date', models.DateField()),
                ('race_class', models.IntegerField()),
                ('race_number', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('starters', models.IntegerField()),
                ('rank', models.IntegerField(null=True)),
                ('bracket', models.IntegerField(null=True)),
                ('horse_number', models.IntegerField(null=True)),
                ('age', models.IntegerField()),
                ('jockey_weight', models.IntegerField(null=True)),
                ('race_time', models.FloatField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('odds', models.FloatField(null=True)),
                ('three_halon', models.FloatField(null=True)),
                ('first_corner_rank', models.FloatField(null=True)),
                ('second_corner_rank', models.FloatField(null=True)),
                ('third_corner_rank', models.FloatField(null=True)),
                ('fourth_corner_rank', models.FloatField(null=True)),
                ('horse_weight', models.IntegerField(null=True)),
                ('horse_weight_change', models.IntegerField(null=True)),
                ('direction',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='race_info.direction')),
                ('gender',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='race_info.gender')),
                ('horse',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_info.horse')),
                ('jockey',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_info.jockey')),
                ('trace_condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                      to='race_info.trackcondition')),
                ('trace_type',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='race_info.tracktype')),
                ('trainer',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_info.trainer')),
                ('training_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                      to='race_info.trainingcenter')),
                ('venue',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='race_info.venue')),
                ('weather',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='race_info.weather')),
            ],
            options={
                'verbose_name': 'レース成績',
                'verbose_name_plural': 'レース成績',
            },
        ),
        migrations.AddConstraint(
            model_name='race',
            constraint=models.UniqueConstraint(fields=('race_id', 'horse'), name='race_unique'),
        ),
    ]
