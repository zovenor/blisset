# Generated by Django 4.1.3 on 2022-12-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_rename_color_clothesmodel_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothesmodel',
            name='article',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothesmodel',
            name='composition',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothesmodel',
            name='construction',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothesmodel',
            name='features',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]