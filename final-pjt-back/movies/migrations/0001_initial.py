# Generated by Django 3.2.12 on 2022-05-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50)),
                ('character', models.CharField(max_length=50)),
                ('profile_path', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.IntegerField()),
                ('genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(null=True)),
                ('released_date', models.DateField(null=True)),
                ('poster_path', models.CharField(max_length=300, null=True)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('popularity', models.FloatField()),
                ('video_path', models.CharField(max_length=300, null=True)),
                ('actors', models.ManyToManyField(related_name='actor_movie', to='movies.Actor')),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('recommend_movies', models.ManyToManyField(related_name='recommended', to='movies.Movie')),
            ],
        ),
    ]