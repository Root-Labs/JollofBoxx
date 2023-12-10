from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Movie, TvSerie, Season, Episode
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from django.db.models import Q

# Create your views here.

#This function redirects clients to the home page when an invalid path is entered in the url
def handle404(request, exception):
    return HttpResponseRedirect('home')

#Hompage View
def Home(request):
    movies= Movie.objects.all().order_by('-release_date')[:5]
    series= TvSerie.objects.all()
    
    if request.method== "POST":
        search= request.POST["search"]
        search= search.upper()
        return redirect('search', search=search)
    return render(request, "index.html", {"movies": movies, "series":series})


def SearchResults(request, search):
    if request.method== "POST":
        search= request.POST["search"]
        search= search.upper()
        return redirect('search', search=search)
    
    if search:
        results = []

        all_movies = Movie.objects.all()
        for movies in all_movies:
            similarity_ratio= fuzz.ratio(search, movies.title)
            if similarity_ratio> 50:
                results.append((movies, similarity_ratio))

        all_tv_series = TvSerie.objects.all()
        for tv_serie in all_tv_series:
            similarity_ratio = fuzz.ratio(search, tv_serie.title)
            if similarity_ratio > 50:
                results.append((tv_serie, similarity_ratio))

        results.sort(key=lambda x: x[1], reverse=True)
        results = [result[0] for result in results]


    movies= Movie.objects.all().order_by('-release_date')[:6]
    return render(request, "search.html", {"search":search, "results": results, "movies": movies})


def movie(request, title):
    movie= Movie.objects.get(title=title)
    genres= movie.genres.all()

    if request.method== "POST":
        search= request.POST["search"]
        search= search.upper()
        return redirect('search', search=search)
    
    return render(request, "movie.html", {"movie": movie, "genres":genres})



def series(request, title):
    series= TvSerie.objects.get(title=title)
    seasons = Season.objects.filter(series=series)
    genres= series.genres.all()
    episodes = Episode.objects.filter(season__in=seasons)

    if request.method== "POST":
        search= request.POST["search"]
        search= search.upper()
        return redirect('search', search=search)
    
    return render(request, "series.html", {"series": series, "episodes":episodes, "genres":genres})


def misc(request):
    return render(request, "misc.html")