class Movie:
    def __init__(self, title, cast, category, release_date, budget, year, genre, director, rating):
        self.title = title
        self.cast = cast
        self.category = category
        self.release_date = release_date
        self.budget = budget
        self.year = year
        self.genre = genre
        self.director = director
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __repr__(self):
        return f"Movie(title={self.title}, year={self.year}, genre={self.genre}, director={self.director}, rating={self.rating})"

    def details(self):
        return f"Title: {self.title}, Cast: {', '.join(self.cast)}, Category: {self.category}, Release Date: {self.release_date}, Budget: ${self.budget}"
