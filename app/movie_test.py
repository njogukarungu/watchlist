import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    def setUp(self):
        self.newMovie = Movie(123, "Python must be crazy", 'A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.newMovie,Movie))
    
if __name__ == "__main__":
    unittest.main()