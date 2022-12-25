# Generated by Django 4.1.3 on 2022-12-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_photomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothesmodel',
            name='photos',
            field=models.ManyToManyField(to='main.photomodel'),
        ),
        migrations.AddField(
            model_name='photomodel',
            name='name',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]