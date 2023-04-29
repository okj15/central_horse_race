# Generated by Django 3.2.5 on 2021-08-03 00:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('basic_info', '0003_horse_stallion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='breeder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_info.breeder'),
        ),
        migrations.AlterField(
            model_name='horse',
            name='father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sire',
                                    to='basic_info.stallion'),
        ),
        migrations.AlterField(
            model_name='horse',
            name='mother_father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bms',
                                    to='basic_info.stallion'),
        ),
        migrations.AlterField(
            model_name='horse',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_info.owner'),
        ),
    ]
