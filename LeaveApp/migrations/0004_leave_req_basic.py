# Generated by Django 4.2.7 on 2024-04-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0003_leave_req_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_req',
            name='basic',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]