# Generated by Django 4.0.4 on 2022-05-27 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='preamble',
            new_name='intro',
        ),
    ]
