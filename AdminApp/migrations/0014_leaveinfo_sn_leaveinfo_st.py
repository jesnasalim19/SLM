# Generated by Django 4.2.7 on 2024-04-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0013_remove_leaveinfo_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveinfo',
            name='sn',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leaveinfo',
            name='st',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
