# Generated by Django 4.2.7 on 2024-04-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0006_leave_req_st'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_req',
            name='lop',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
