# Generated by Django 3.2 on 2022-10-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_committer_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='committer_company_statistic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('total', models.IntegerField()),
                ('update_time', models.DateTimeField()),
            ],
        ),
    ]
