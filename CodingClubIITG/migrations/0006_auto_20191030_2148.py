# Generated by Django 2.2.4 on 2019-10-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodingClubIITG', '0005_members_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='img',
            field=models.FileField(upload_to='members/'),
        ),
    ]
