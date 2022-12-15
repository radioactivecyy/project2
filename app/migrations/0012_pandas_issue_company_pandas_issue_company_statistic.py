# Generated by Django 3.2 on 2022-11-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20221101_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='pandas_issue_company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('node_id', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=128)),
                ('get_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='pandas_issue_company_statistic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('total', models.IntegerField()),
                ('update_time', models.DateTimeField()),
            ],
        ),
    ]