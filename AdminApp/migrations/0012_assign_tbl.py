# Generated by Django 4.2.7 on 2024-04-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0011_payroll_tbl_al_payroll_tbl_st'),
    ]

    operations = [
        migrations.CreateModel(
            name='assign_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=25)),
                ('start', models.CharField(max_length=25)),
                ('end', models.CharField(max_length=25)),
                ('nl', models.IntegerField()),
                ('fn', models.CharField(max_length=25)),
            ],
        ),
    ]