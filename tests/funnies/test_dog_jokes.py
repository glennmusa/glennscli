from unittest import TestCase
from src.mypypackage.funnies import dog_jokes

class TestDogJokes(TestCase):
    def test_returns_a_joke(self):
        joke_result = dog_jokes.get_joke()
        self.assertTrue(dog_jokes.jokes.__contains__(joke_result))
