from unittest import TestCase
from src.glennscli.funnies import cat_jokes

class TestCatJokes(TestCase):
    def test_returns_a_joke(self):
        joke_result = cat_jokes.get_jokes(1)[0]
        self.assertTrue(cat_jokes.jokes.__contains__(joke_result))

    def test_numjokes_greater_than_length(self):
        joke_result = cat_jokes.get_jokes(100)
        self.assertEqual(len(joke_result), len(cat_jokes.jokes))
        self.assertTrue(set(cat_jokes.jokes) == set(joke_result))

    def test_numjokes_less_than_zero(self):
        joke_result = cat_jokes.get_jokes(-100)
        self.assertEqual(len(joke_result), 1)
        self.assertTrue(cat_jokes.jokes.__contains__(joke_result[0]))


    def test_numjokes_zero(self):
        joke_result = cat_jokes.get_jokes(0)
        self.assertEqual(len(joke_result), 1)
        self.assertTrue(cat_jokes.jokes.__contains__(joke_result[0]))
