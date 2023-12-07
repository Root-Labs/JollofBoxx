# Generated by Django 4.2.8 on 2023-12-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jollof_box', '0013_alter_movie_star_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='star_rating',
            field=models.CharField(choices=[('⭐', 3), ('⭐', '⭐')], max_length=50, null=True, verbose_name='Star rating'),
        ),
    ]