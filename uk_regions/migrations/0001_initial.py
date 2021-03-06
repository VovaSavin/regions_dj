# Generated by Django 3.2.8 on 2021-11-02 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReDicKoatuuRegion',
            fields=[
                ('this_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('level', models.PositiveIntegerField(verbose_name='Уровень')),
                ('name', models.CharField(max_length=100, verbose_name='Область')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Областя',
            },
        ),
        migrations.CreateModel(
            name='ReDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(verbose_name='Уровень')),
                ('name', models.CharField(max_length=100)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region', to='uk_regions.redickoatuuregion', verbose_name='Область')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='RegionCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(verbose_name='Уровень')),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district', to='uk_regions.redistrict', verbose_name='Район')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regionfordistrict', to='uk_regions.redickoatuuregion', verbose_name='Область')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
    ]
