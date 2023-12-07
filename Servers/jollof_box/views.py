from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Movie, TvSerie, Season, Episode
from fuzzywuzzy import fuzz

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
        film= request.POST["film"]
        return redirect('search', search=search, film=film)
    return render(request, "index.html", {"movies": movies, "series":series})


def SearchResults(request, film, search):
    if film == "movies":
        all_movies = Movie.objects.all()
        results = []
        for movies in all_movies:
            similarity_ratio= fuzz.ratio(search, movies.title)
            if similarity_ratio> 60:
                results.append((movies, similarity_ratio))
        results.sort(key=lambda x: x[1], reverse=True)
        results = [result[0] for result in results]


    elif film== "series":
        all_tv_series = TvSerie.objects.all()
        results = []
        for tv_serie in all_tv_series:
            similarity_ratio = fuzz.ratio(search, tv_serie.title)
            if similarity_ratio > 70:
                results.append((tv_serie, similarity_ratio))
        results.sort(key=lambda x: x[1], reverse=True)
        results = [result[0] for result in results]

    else:
        pass

    return render(request, "search.html", {"results": results, "film": film})


def movie(request, title):
    movie= Movie.objects.get(title=title)
    genres= movie.genres.all()

    if request.method== "POST":
        search= request.POST["search"]
        search= search.upper()
        film=request.POST["film"]
        return redirect('search', search=search, film=film)
    
    return render(request, "movie.html", {"movie": movie, "genres":genres})



def series(request, title):
    series= TvSerie.objects.get(title=title)
    seasons = Season.objects.filter(series=series)
    genres= series.genres.all()
    episodes = Episode.objects.filter(season__in=seasons)

    if request.method== "POST":
        search= request.POST["search"]
        search= search.upper()
        film=request.POST["film"]
        return redirect('search', search=search, film=film)
    
    return render(request, "series.html", {"series": series, "episodes":episodes, "genres":genres})


def misc(request):
    return render(request, "misc.html")