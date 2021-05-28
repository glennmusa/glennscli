from unittest import TestCase
from src.mypypackage.funnies import cat_jokes

class TestCatJokes(TestCase):
    def test_returns_a_joke(self):
        joke_result = cat_jokes.get_joke()
        self.assertTrue(cat_jokes.jokes.__contains__(joke_result))
