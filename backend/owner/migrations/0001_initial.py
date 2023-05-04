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
                'verbose_name': '馬主マスタ',
                'verbose_name_plural': '馬主マスタ',
            },
        ),
        migrations.CreateModel(
            name='OwnerResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('first', models.IntegerField()),
                ('second', models.IntegerField()),
                ('third', models.IntegerField()),
                ('unplaced', models.IntegerField()),
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
                ('quinella_rate', models.FloatField()),
                ('show_rate', models.FloatField()),
                ('earnings', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.master')),
            ],
            options={
                'verbose_name': '馬主成績',
                'verbose_name_plural': '馬主成績',
            },
        ),
        migrations.AddConstraint(
            model_name='ownerresult',
            constraint=models.UniqueConstraint(fields=('year', 'owner'), name='owner_result_unique'),
        ),
    ]
