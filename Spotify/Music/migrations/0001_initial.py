# Generated by Django 4.2.7 on 2023-11-29 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='artist_images/')),
                ('Age', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('duration', models.DurationField()),
                ('image', models.ImageField(upload_to='song_images/')),
                ('release_date', models.DateField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.artist')),
                ('other_artists', models.ManyToManyField(blank=True, related_name='featured_songs', to='Music.artist')),
            ],
        ),
    ]
