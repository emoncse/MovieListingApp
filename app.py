from user import User


class MovieManager:
    def __init__(self):
        self.movies = []
        self.users = {}

    def add_movie(self, movie):
        self.movies.append(movie)

    def register_user(self, name, email):
        if (name, email) not in self.users:
            self.users[(name, email)] = User(name, email)
        return self.users[(name, email)]

    def search_movies(self, query):
        matching_movies = [movie for movie in self.movies if self.movie_matches_query(movie, query)]
        return sorted(matching_movies, key=lambda movie: movie.title)

    def movie_matches_query(self, movie, query):
        query_lower = query.lower()
        return (query_lower in movie.title.lower() or
                any(query_lower in actor.lower() for actor in movie.cast) or
                query_lower in movie.category.lower() or
                query_lower in movie.genre.lower() or
                query_lower in movie.director.lower() or
                str(movie.year) == query_lower or
                str(movie.rating) == query_lower)
