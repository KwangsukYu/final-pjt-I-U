# Generated by Django 3.2.12 on 2022-05-25 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_recommend_movies'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='movie_title',
        ),
        migrations.RemoveField(
            model_name='article',
            name='rank',
        ),
        migrations.AddField(
            model_name='article',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='movies.movie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
