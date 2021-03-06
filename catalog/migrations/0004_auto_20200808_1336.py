# Generated by Django 3.0.6 on 2020-08-08 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_book_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Select a language for this book', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]
