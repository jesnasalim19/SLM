# Generated by Django 4.2.7 on 2024-04-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_admin_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='payroll_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=25)),
                ('lt', models.CharField(max_length=25)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('wd', models.IntegerField()),
                ('nl', models.IntegerField()),
                ('basic', models.IntegerField()),
                ('lop', models.IntegerField()),
                ('net', models.IntegerField()),
            ],
        ),
    ]