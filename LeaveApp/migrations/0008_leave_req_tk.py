# Generated by Django 4.2.4 on 2024-04-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0007_leave_req_lop'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_req',
            name='tk',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]