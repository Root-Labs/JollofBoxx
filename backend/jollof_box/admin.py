from django.contrib import admin
from .models import Movie, TvSerie, Season, Episode, Genre

class MovieDisplay(admin.ModelAdmin):
    list_display = ("title", "rating", "download")


# Register your models here.
admin.site.register(Movie, MovieDisplay)
admin.site.register(TvSerie)
admin.site.register(Season)
admin.site.register(Episode)
admin.site.register(Genre)