# Generated by Django 4.1.3 on 2022-12-18 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_configsmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectionmodel',
            options={'verbose_name': 'Коллекции'},
        ),
        migrations.AlterModelOptions(
            name='configsmodel',
            options={'verbose_name': 'Конфигурация'},
        ),
    ]