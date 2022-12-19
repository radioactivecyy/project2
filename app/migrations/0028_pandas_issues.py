# Generated by Django 3.2 on 2022-12-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_pytorch_issues'),
    ]

    operations = [
        migrations.CreateModel(
            name='pandas_issues',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('closed_at', models.DateTimeField(default=None, null=True)),
                ('comment_cnt', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=512)),
            ],
        ),
    ]