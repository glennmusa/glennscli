import sys
import pytest
from _pytest.capture import capsys
from unittest import TestCase, mock
import src.mypypackage.command_line as command_line
from src.mypypackage.funnies import dog_jokes
from src.mypypackage.funnies import cat_jokes

class TestCli(TestCase):
    def test_dog_jokes(self):
        with mock.patch.object(sys, 'argv', ['the_app_name_is_always_arg_0', 'dog']):
            command_line.main()
            out, err = self.capsys.readouterr()
            self.assertTrue(dog_jokes.jokes.__contains__(out.rstrip()))
            self.assertEqual(err, '')

    def test_cat_jokes(self):
        with mock.patch.object(sys, 'argv', ['the_app_name_is_always_arg_0', 'cat']):
            command_line.main()
            out, err = self.capsys.readouterr()
            self.assertTrue(cat_jokes.jokes.__contains__(out.rstrip()))
            self.assertEqual(err, '')

    def test_help_when_unknown_args(self):
        with mock.patch.object(sys, 'argv', ['the_app_name_is_always_arg_0', 'foo']):
            command_line.main()
            out, err = self.capsys.readouterr()
            self.assertEqual(out.rstrip(), command_line.help_message)
            self.assertEqual(err, '')

    def test_help_when_no_args(self):
        with mock.patch.object(sys, 'argv', ['the_app_name_is_always_arg_0']):
            command_line.main()
            out, err = self.capsys.readouterr()
            self.assertEqual(out.rstrip(), command_line.help_message)
            self.assertEqual(err, '')

    # https://github.com/pytest-dev/pytest/issues/2504#issuecomment-309475790
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys
