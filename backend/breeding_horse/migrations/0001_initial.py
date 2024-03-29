# Generated by Django 4.2 on 2023-05-01 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': '繁殖馬マスタ',
                'verbose_name_plural': '繁殖馬マスタ',
            },
        ),
        migrations.CreateModel(
            name='SireResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('foals', models.IntegerField()),
                ('winners', models.IntegerField()),
                ('runs', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('graded_runs', models.IntegerField()),
                ('graded_wins', models.IntegerField()),
                ('special_runs', models.IntegerField()),
                ('special_wins', models.IntegerField()),
                ('general_runs', models.IntegerField()),
                ('general_wins', models.IntegerField()),
                ('turf_runs', models.IntegerField()),
                ('turf_wins', models.IntegerField()),
                ('dirt_runs', models.IntegerField()),
                ('dirt_wins', models.IntegerField()),
                ('win_rate', models.FloatField()),
                ('ei', models.FloatField()),
                ('earnings', models.FloatField()),
                ('turf_average_distance', models.FloatField()),
                ('dirt_average_distance', models.FloatField()),
                ('sire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sire_result', to='breeding_horse.master')),
            ],
            options={
                'verbose_name': '種牡馬成績',
                'verbose_name_plural': '種牡馬成績',
            },
        ),
        migrations.CreateModel(
            name='BmsResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('foals', models.IntegerField()),
                ('winners', models.IntegerField()),
                ('runs', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('graded_runs', models.IntegerField()),
                ('graded_wins', models.IntegerField()),
                ('special_runs', models.IntegerField()),
                ('special_wins', models.IntegerField()),
                ('general_runs', models.IntegerField()),
                ('general_wins', models.IntegerField()),
                ('turf_runs', models.IntegerField()),
                ('turf_wins', models.IntegerField()),
                ('dirt_runs', models.IntegerField()),
                ('dirt_wins', models.IntegerField()),
                ('win_rate', models.FloatField()),
                ('ei', models.FloatField()),
                ('earnings', models.FloatField()),
                ('turf_average_distance', models.FloatField(null=True)),
                ('dirt_average_distance', models.FloatField(null=True)),
                ('bms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bms_result', to='breeding_horse.master')),
            ],
            options={
                'verbose_name': '父母成績',
                'verbose_name_plural': '父母成績',
            },
        ),
        migrations.AddConstraint(
            model_name='sireresult',
            constraint=models.UniqueConstraint(fields=('year', 'sire'), name='sire_result_unique'),
        ),
        migrations.AddConstraint(
            model_name='bmsresult',
            constraint=models.UniqueConstraint(fields=('year', 'bms'), name='bms_result_unique'),
        ),
    ]
