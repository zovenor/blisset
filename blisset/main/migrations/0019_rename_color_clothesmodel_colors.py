# Generated by Django 4.1.3 on 2022-12-24 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_clothesmodel_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothesmodel',
            old_name='color',
            new_name='colors',
        ),
    ]