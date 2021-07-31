# Generated by Django 2.2.20 on 2021-07-31 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredVoter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='VotingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date_of_event', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.RegisteredVoter', unique=True)),
                ('voting_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.VotingEvent')),
            ],
        ),
        migrations.AddField(
            model_name='registeredvoter',
            name='voting_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.VotingEvent'),
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('of_type', models.CharField(max_length=20)),
                ('party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='votes.Party')),
            ],
        ),
    ]
