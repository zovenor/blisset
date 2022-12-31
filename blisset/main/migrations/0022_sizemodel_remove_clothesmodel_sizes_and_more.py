# Generated by Django 4.1.3 on 2022-12-31 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_mainpageslider1model_mainpageslider2model'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.RemoveField(
            model_name='clothesmodel',
            name='sizes',
        ),
        migrations.AddField(
            model_name='clothesmodel',
            name='sizes',
            field=models.ManyToManyField(to='main.sizemodel'),
        ),
    ]
