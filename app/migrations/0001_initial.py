# Generated by Django 4.0.4 on 2022-12-20 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='commit_by_day',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('comm_cnt', models.IntegerField(default=0)),
                ('desi_cnt', models.IntegerField(default=0)),
                ('modi_files', models.IntegerField(default=0)),
                ('modi_del', models.CharField(max_length=128)),
                ('modi_ins', models.CharField(max_length=128)),
                ('modi_files_core', models.IntegerField(default=0)),
                ('comm_cnt_core', models.IntegerField(default=0)),
                ('desi_cnt_core', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='commit_contributors',
            fields=[
                ('author', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('modi_files', models.IntegerField(default=0)),
                ('modi_del', models.IntegerField(default=0)),
                ('modi_ins', models.IntegerField(default=0)),
                ('if_core', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='commit_update',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_update', models.DateTimeField(default=None)),
                ('time_last_record', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='committer_company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('node_id', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=128)),
                ('get_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='committer_company_statistic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('total', models.IntegerField()),
                ('update_time', models.DateTimeField()),
                ('duplicate', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='issue_company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('node_id', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=128)),
                ('get_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='issue_company_statistic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('total', models.IntegerField()),
                ('update_time', models.DateTimeField()),
                ('duplicate', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pandas_commit_by_day',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('comm_cnt', models.IntegerField(default=0)),
                ('desi_cnt', models.IntegerField(default=0)),
                ('modi_files', models.IntegerField(default=0)),
                ('modi_del', models.CharField(max_length=128)),
                ('modi_ins', models.CharField(max_length=128)),
                ('modi_files_core', models.IntegerField(default=0)),
                ('comm_cnt_core', models.IntegerField(default=0)),
                ('desi_cnt_core', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='pandas_commit_contributors',
            fields=[
                ('author', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('modi_files', models.IntegerField(default=0)),
                ('modi_del', models.IntegerField(default=0)),
                ('modi_ins', models.IntegerField(default=0)),
                ('if_core', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='pandas_commit_update',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_update', models.DateTimeField(default=None)),
                ('time_last_record', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='pandas_committer_company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('node_id', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=128)),
                ('get_time', models.DateTimeField()),
            ],
        ),
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
            name='pandas_issues',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('closed_at', models.DateTimeField(default=None, null=True)),
                ('comment_cnt', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='pandas_stargazer_company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('node_id', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=128)),
                ('get_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='pandas_total',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=128)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pytorch_issues',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('closed_at', models.DateTimeField(default=None, null=True)),
                ('comment_cnt', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='stargazer_company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('node_id', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=128)),
                ('get_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='stargazer_company_statistic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('total', models.IntegerField()),
                ('update_time', models.DateTimeField()),
                ('duplicate', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='total',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=128)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pandas_commit_history',
            fields=[
                ('hash', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('author_email', models.CharField(max_length=128)),
                ('committer', models.CharField(max_length=128)),
                ('committer_email', models.CharField(max_length=128)),
                ('time_local', models.DateTimeField(default=None)),
                ('commit_time', models.DateTimeField(default=None)),
                ('commit_intro', models.CharField(max_length=512)),
                ('commit_keyword', models.CharField(max_length=64)),
                ('if_design', models.BooleanField(default=False)),
                ('modi_files', models.IntegerField(default=0)),
                ('modi_del', models.IntegerField(default=0)),
                ('modi_ins', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.pandas_commit_contributors')),
            ],
        ),
        migrations.CreateModel(
            name='commit_history',
            fields=[
                ('hash', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('author_email', models.CharField(max_length=128)),
                ('committer', models.CharField(max_length=128)),
                ('committer_email', models.CharField(max_length=128)),
                ('time_local', models.DateTimeField(default=None)),
                ('commit_time', models.DateTimeField(default=None)),
                ('commit_intro', models.CharField(max_length=512)),
                ('commit_keyword', models.CharField(max_length=64)),
                ('if_design', models.BooleanField(default=False)),
                ('modi_files', models.IntegerField(default=0)),
                ('modi_del', models.IntegerField(default=0)),
                ('modi_ins', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.commit_contributors')),
            ],
        ),
    ]
