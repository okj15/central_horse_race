# Generated by Django 4.2 on 2023-05-01 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jockey', '0001_initial'),
        ('trainer', '0001_initial'),
        ('breeding_horse', '0001_initial'),
        ('owner', '0001_initial'),
        ('breeder', '0001_initial'),
        ('race', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('birthday', models.DateField()),
                ('mother_id', models.TextField()),
                ('father_father_id', models.TextField()),
                ('father_mother_id', models.TextField()),
                ('mother_mother_id', models.TextField()),
                ('breeder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='breeder.master')),
                ('father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sire', to='breeding_horse.master')),
                ('mother_father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bms', to='breeding_horse.master')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='owner.master')),
            ],
            options={
                'verbose_name': '競走馬マスタ',
                'verbose_name_plural': '競走馬マスタ',
            },
        ),
        migrations.CreateModel(
            name='RaceResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(null=True)),
                ('bracket', models.IntegerField(null=True)),
                ('horse_number', models.IntegerField(null=True)),
                ('gender', models.IntegerField(choices=[(1, '牡'), (2, '牝'), (3, 'セ')], null=True)),
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
                ('training_center', models.IntegerField(choices=[(1, '美浦'), (2, '栗東')], null=True)),
                ('horse_weight', models.IntegerField(null=True)),
                ('horse_weight_change', models.IntegerField(null=True)),
                ('horse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='racing_horse.master')),
                ('jockey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jockey.master')),
                ('race_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='race.race')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainer.master')),
            ],
            options={
                'verbose_name': 'レース成績',
                'verbose_name_plural': 'レース成績',
            },
        ),
        migrations.AddConstraint(
            model_name='raceresult',
            constraint=models.UniqueConstraint(fields=('race_id', 'horse'), name='race_result_unique'),
        ),
    ]