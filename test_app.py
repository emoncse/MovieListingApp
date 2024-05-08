import unittest
from models import Movie
from user import User
from app import MovieManager


class TestMovieApp(unittest.TestCase):
    def setUp(self):
        self.movie_manager = MovieManager()
        self.user = self.movie_manager.register_user("Imran", "imran.uapcse@gmail.com")
        self.movie = Movie(
            title="3 Idiots",
            cast=["Aamir Khan", "R. Madhavan", "Sharman Joshi", "Kareena Kapoor"],
            category="Comedy/Drama",
            release_date="2009-12-25",
            budget=55000000,
            year=2009,
            genre="Comedy/Drama",
            director="Rajkumar Hirani",
            rating=8.4
        )
        self.movie_manager.add_movie(self.movie)

    def test_add_movie(self):
        self.assertIn(self.movie, self.movie_manager.movies)

    def test_register_user(self):
        self.assertEqual(self.user.name, "Imran")
        self.assertEqual(self.user.email, "imran.uapcse@gmail.com")
        self.assertIsInstance(self.user, User)

    def test_add_to_favorites(self):
        self.user.add_to_favorites(self.movie)
        self.assertIn(self.movie, self.user.favorite_movies)

    def test_remove_from_favorites(self):
        self.user.add_to_favorites(self.movie)
        self.user.remove_from_favorites(self.movie)
        self.assertNotIn(self.movie, self.user.favorite_movies)

    def test_search_movies(self):
        results = self.movie_manager.search_movies("3 Idiots")
        self.assertTrue(any("3 Idiots" in result for result in results))

    def test_search_favorites(self):
        self.user.add_to_favorites(self.movie)
        results = self.user.search_favorites("3 Idiots")
        self.assertTrue(any("3 Idiots" in movie.title for movie in results))

    def test_movie_details(self):
        expected_details = ("Title: 3 Idiots, Year: 2009, Genre: Comedy/Drama, Director: Rajkumar Hirani, "
                            "Rating: 8.4, Cast: Aamir Khan, R. Madhavan, Sharman Joshi, Kareena Kapoor, "
                            "Category: Comedy/Drama, Release Date: 2009-12-25, Budget: $55000000")
        self.assertEqual(expected_details, self.movie.details())


if __name__ == "__main__":
    unittest.main()
