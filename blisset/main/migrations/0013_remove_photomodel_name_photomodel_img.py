# Generated by Django 4.1.3 on 2022-12-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_photomodel_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photomodel',
            name='name',
        ),
        migrations.AddField(
            model_name='photomodel',
            name='img',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]