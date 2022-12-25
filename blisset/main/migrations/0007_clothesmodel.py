# Generated by Django 4.1.3 on 2022-12-23 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_instagrammodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.collectionmodel')),
            ],
        ),
    ]