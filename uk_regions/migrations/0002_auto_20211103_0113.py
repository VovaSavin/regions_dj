# Generated by Django 3.2.8 on 2021-11-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uk_regions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redistrict',
            name='id',
        ),
        migrations.AddField(
            model_name='redistrict',
            name='this_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='Идентификатор'),
            preserve_default=False,
        ),
    ]