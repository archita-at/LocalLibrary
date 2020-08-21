# Generated by Django 3.0.6 on 2020-08-21 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20200821_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book. To select multiple genres, press Ctrl and select multiple genres.', to='catalog.Genre'),
        ),
    ]