class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.favorite_movies = []

    def __str__(self):
        return f'{self.name} <{self.email}>'

    def add_to_favorites(self, movie):
        self.favorite_movies.append(movie)

    def remove_from_favorites(self, movie):
        self.favorite_movies.remove(movie)

    def display_favorites(self):
        return self.favorite_movies

    def search_favorites(self, query):
        return sorted(
            [movie for movie in self.favorite_movies if query.lower() in movie.title.lower() or
             any(query.lower() in actor.lower() for actor in movie.cast) or
             query.lower() in movie.category.lower()],
            key=lambda x: x.title
        )
