# Generated by Django 3.2 on 2022-12-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20221217_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='pytorch_issue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
                ('closed_at', models.DateTimeField(default=None)),
                ('comment_cnt', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Commits',
        ),
        migrations.DeleteModel(
            name='Contributors',
        ),
        migrations.DeleteModel(
            name='date01',
        ),
    ]