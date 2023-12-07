from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


GENRE_CHOICES = [
    ('Action', 'Action'),
    ('Horror', 'Horror'),
    ('Drama', 'Drama'),
    ('Thriller', 'Thriller'),
    ('Comedy', 'Comedy'),
    ('Sci-fi', 'Science Fiction'),
    ('Romance', 'Romance'),
    ('Adventure', 'Adventure'),
    ('Fantasy', 'Fantasy'),
    ('Animation', 'Animation'),
    ('Musical', 'Musical'),
    ('Mystery', 'Mystery')
]

INDUSTRY_CHOICES = [
    ('Hollywood', 'Hollywood'),
    ('Nollywood', 'Nollywood'),
]

RATING = [
    ('⭐', 1),
    ('⭐⭐', 2),
    ('⭐⭐⭐', 3),
    ('⭐⭐⭐⭐', 4),
    ('⭐⭐⭐⭐⭐', 5),
]


class Genre(models.Model):
    genre= models.CharField(("Genre"), choices=GENRE_CHOICES, max_length=50)

    def __str__(self):
        return self.genre
    

class Movie(models.Model):
    title= models.CharField(("Title"), max_length=100, null=True)
    poster= models.CharField(("Poster"), max_length=500, null=True)
    summary= models.TextField(("Summary"), max_length=500, null=True)
    trailer= models.CharField(("Trailer Link"), max_length=100, null=True)
    download= models.CharField(("Download Link"), max_length=100, null=True)
    rating= models.PositiveIntegerField(("Rating"), null=True)
    release_date = models.DateField(("Release Date"), null=True)
    genres = models.ManyToManyField(Genre)
    trending= models.PositiveIntegerField(("Trending"), null=True)
    language= models.CharField(("Language"), max_length=100, null=True)
    industry= models.CharField(("Industry"), choices=INDUSTRY_CHOICES, max_length=50, null=True)
    runtime= models.CharField(("Runtime"), null=True, max_length=50)
    company= models.CharField(("Company"), null=True, max_length=50)
    star_rating= models.CharField(("Star rating"), choices=RATING,  max_length=50, null=True)

    def __str__(self):
        return self.title
    

    
class TvSerie(models.Model):
    title= models.CharField(("Title"), max_length=100, null=True)
    poster= models.CharField(("Poster"), max_length=500, null=True)
    summary= models.TextField(("Summary"), max_length=500, null=True)
    genres = models.ManyToManyField(Genre)
    language= models.CharField(("Language"), max_length=100, null=True)
    release_date = models.DateField(("Release Date"), null=True)
    company= models.CharField(("Company"), null=True, max_length=50)
    industry= models.CharField(("Industry"), choices=INDUSTRY_CHOICES, null=True, max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
    


class Season(models.Model):
    series = models.ForeignKey(TvSerie, on_delete=models.CASCADE)
    season = models.PositiveIntegerField(("Season"), null=True)

    def __str__(self):
        return f"{self.series.title} - Season {self.season}"
    
    class Meta:
        ordering = ['series', 'season']
    


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episode = models.PositiveIntegerField(("Episode"), null=True)
    download= models.CharField(("Download Link"), max_length=100, null=True)
    rating= models.PositiveIntegerField(("Rating"), null=True)
    star_rating= models.CharField(("Star rating"), choices=RATING,  max_length=50, null=True)

    def __str__(self):
        return f"{self.season} - Episode {self.episode}"
    
    class Meta:
        ordering = ['season', 'episode']



@receiver(pre_save, sender=Movie)
@receiver(pre_save, sender=TvSerie)
def convert_name_to_upper(sender, instance, **kwargs):
    instance.title = instance.title.upper()