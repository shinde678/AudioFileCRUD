# Generated by Django 3.2 on 2021-04-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('narrator', models.CharField(max_length=100, null=True)),
                ('duration', models.PositiveIntegerField(max_length=5, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podcast_name', models.CharField(max_length=100, null=True)),
                ('duration', models.PositiveIntegerField(max_length=5, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('participants', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100, null=True)),
                ('duration', models.PositiveIntegerField(max_length=5, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]