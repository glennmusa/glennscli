from unittest import TestCase
from src.glennscli.funnies import dog_jokes

class TestDogJokes(TestCase):
    def test_returns_a_joke(self):
        joke_result = dog_jokes.get_jokes(1)[0]
        self.assertTrue(dog_jokes.jokes.__contains__(joke_result))

    def test_numjokes_greater_than_length(self):
        joke_result = dog_jokes.get_jokes(100)
        self.assertEqual(len(joke_result), len(dog_jokes.jokes))
        self.assertTrue(set(dog_jokes.jokes) == set(joke_result))

    def test_numjokes_less_than_zero(self):
        joke_result = dog_jokes.get_jokes(-100)
        self.assertEqual(len(joke_result), 1)
        self.assertTrue(dog_jokes.jokes.__contains__(joke_result[0]))

    def test_numjokes_zero(self):
        joke_result = dog_jokes.get_jokes(0)
        self.assertEqual(len(joke_result), 1)
        self.assertTrue(dog_jokes.jokes.__contains__(joke_result[0]))
