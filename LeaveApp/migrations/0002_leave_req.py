# Generated by Django 4.2.7 on 2024-04-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=25)),
                ('lt', models.CharField(max_length=25)),
                ('md', models.FileField(upload_to='medical')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('rs', models.TextField()),
                ('rd', models.IntegerField()),
                ('al', models.IntegerField()),
                ('rm', models.IntegerField()),
            ],
        ),
    ]
