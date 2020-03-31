from app import app
from flask import render_template
from .request import getMovies

@app.route('/')
def index():
    popular_movies = getMovies('popular')
    upcoming_movie = getMovies('upcoming')
    now_showing_movie = getMovies('now_playing')
    print(popular_movies)
    title = "Welcome to the popular movies"
    return render_template("index.html", title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

    #upcoming = upcoming_movies, now_showing = now_showing_movies