# Generated by Django 2.2.4 on 2019-10-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodingClubIITG', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='year',
            field=models.IntegerField(default=2019),
            preserve_default=False,
        ),
    ]
