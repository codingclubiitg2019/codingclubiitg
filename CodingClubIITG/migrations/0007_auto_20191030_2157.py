# Generated by Django 2.2.4 on 2019-10-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodingClubIITG', '0006_auto_20191030_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.FileField(default=' ', upload_to='events/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='img',
            field=models.FileField(default=' ', upload_to='projects/'),
            preserve_default=False,
        ),
    ]
