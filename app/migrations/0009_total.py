# Generated by Django 3.2 on 2022-10-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_committer_company_statistic'),
    ]

    operations = [
        migrations.CreateModel(
            name='total',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=128)),
                ('total', models.IntegerField()),
            ],
        ),
    ]
