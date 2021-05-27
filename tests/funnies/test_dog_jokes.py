from unittest import TestCase
from src.mypypackage.funnies import dog_jokes

class TestDogJokes(TestCase):
    def test_nose_is_awful(self):
        joke_result = dog_jokes.what_about_the_nose()
        self.assertTrue(joke_result.lower().__contains__("awful"))