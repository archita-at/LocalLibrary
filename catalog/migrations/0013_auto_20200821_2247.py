# Generated by Django 3.0.6 on 2020-08-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20200821_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character ISBN number', max_length=13, verbose_name='ISBN'),
        ),
    ]
