from unittest import TestCase
from src.mypypackage.funnies import cat_jokes

class TestCatJokes(TestCase):
    def test_favorite_show(self):
        joke_result = cat_jokes.whats_their_favorite_show()
        self.assertTrue(joke_result.lower().__contains__("claw and order"))
