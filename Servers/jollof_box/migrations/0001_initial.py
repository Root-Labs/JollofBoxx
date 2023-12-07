# Generated by Django 4.1.6 on 2023-11-23 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genre', models.CharField(choices=[('Action', 'Action'), ('Horror', 'Horror'), ('Drama', 'Drama'), ('Thriller', 'Thriller'), ('Comedy', 'Comedy'), ('Sci-fi', 'Science Fiction'), ('Romance', 'Romance'), ('Adventure', 'Adventure'), ('Fantasy', 'Animation'), ('Musical', 'Musical'), ('Mystery', 'Mystery')], max_length=50, verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='TvSerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('poster', models.CharField(max_length=100, null=True, verbose_name='Poster')),
                ('summary', models.TextField(max_length=500, null=True, verbose_name='Summary')),
                ('industry', models.CharField(choices=[('Hollywood', 'Hollywood'), ('Nollywood', 'Nollywood')], max_length=50, null=True, verbose_name='Industry')),
                ('genres', models.ManyToManyField(to='jollof_box.genre')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.PositiveIntegerField(null=True, verbose_name='Season')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jollof_box.tvserie')),
            ],
            options={
                'ordering': ['series', 'season'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('poster', models.CharField(max_length=100, null=True, verbose_name='Poster')),
                ('Summary', models.TextField(max_length=500, null=True, verbose_name='Summary')),
                ('trailer', models.CharField(max_length=100, null=True, verbose_name='Trailer Link')),
                ('download', models.CharField(max_length=100, null=True, verbose_name='Download Link')),
                ('rating', models.PositiveIntegerField(null=True, verbose_name='Rating')),
                ('release_date', models.DateField(null=True, verbose_name='Release Date')),
                ('trending', models.PositiveIntegerField(null=True, verbose_name='Trending')),
                ('industry', models.CharField(choices=[('Hollywood', 'Hollywood'), ('Nollywood', 'Nollywood')], max_length=50, null=True, verbose_name='Industry')),
                ('genres', models.ManyToManyField(to='jollof_box.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode', models.PositiveIntegerField(null=True, verbose_name='Episode')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Episode Title')),
                ('summary', models.TextField(max_length=500, null=True, verbose_name='Episode Summary')),
                ('release_date', models.DateField(null=True, verbose_name='Release Date')),
                ('Download_link', models.CharField(max_length=100, null=True, verbose_name='Download Link')),
                ('Rating', models.PositiveIntegerField(null=True, verbose_name='Rating')),
                ('Trending', models.PositiveIntegerField(null=True, verbose_name='Trending')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jollof_box.season')),
            ],
            options={
                'ordering': ['season', 'episode'],
            },
        ),
    ]