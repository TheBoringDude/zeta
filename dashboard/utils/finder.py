from dotenv import load_dotenv
import os

# load env vars
load_dotenv()


class Finder:
    def __init__(self) -> None:
        # for searching movies
        self.tmdb_movie_website = f"https://api.themoviedb.org/3/search/movie?api_key={os.getenv('TMDB_API')}&language=en-US&query=[query]&page=1&include_adult=false"
        self.tmdb_img_cdn = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/"
        self.tmdb_series_website = f"https://api.themoviedb.org/3/search/tv?api_key={os.getenv('TMDB_API')}&language=en-US&page=1&query=[query]&include_adult=false"
        self.anime_jikan = "https://api.jikan.moe/v3/search/anime?q=[query]&page=1"
        self.manga_jikan = "https://api.jikan.moe/v3/search/manga?q=[query]&page=1"
        self.kuryana = "https://kuryana.vercel.app/search/q/"
        self.open_library = "http://openlibrary.org/search.json?title=[query]&page=1"