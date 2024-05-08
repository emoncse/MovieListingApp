from app import MovieManager
from models import Movie


def main():
    manager = MovieManager()
    user = manager.register_user("Imran", "imran.uapcse@gmail.com")

    movies = [
        Movie(
            title="3 Idiots",
            cast=["Aamir Khan", "R. Madhavan", "Sharman Joshi", "Kareena Kapoor"],
            category="Comedy/Drama",
            release_date="2009-12-25",
            budget=55000000,
            year=2009,
            genre="Comedy/Drama",
            director="Rajkumar Hirani",
            rating=8.4
        ),
        Movie(
            title="Dangal",
            cast=["Aamir Khan", "Fatima Sana Shaikh", "Sanya Malhotra"],
            category="Biographical/Sport",
            release_date="2016-12-23",
            budget=70000000,
            year=2016,
            genre="Drama",
            director="Nitesh Tiwari",
            rating=8.5
        ),
        Movie(
            title="P.K.",
            cast=["Aamir Khan", "Anushka Sharma", "Sushant Singh Rajput"],
            category="Comedy/Drama/Sci-Fi",
            release_date="2014-12-19",
            budget=85000000,
            year=2014,
            genre="Comedy",
            director="Rajkumar Hirani",
            rating=8.1
        )
    ]

    for movie in movies:
        manager.add_movie(movie)

    user.add_to_favorites(movies[0])
    user.add_to_favorites(movies[2])

    print("Movies in the catalog:")
    for movie_detail in manager.search_movies(""):
        print(movie_detail)

    print("\nUser Favorites:")
    for favorite in user.display_favorites():
        print(favorite)

    print("\nMovies directed by Rajkumar Hirani:")
    for movie_detail in manager.search_movies("Rajkumar Hirani"):
        print(movie_detail)


if __name__ == "__main__":
    main()
