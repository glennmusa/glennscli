import pytest
from _pytest.capture import capsys
from unittest import TestCase
from mypypackage.funnies import dog_jokes
from mypypackage import command_line

class TestConsole(TestCase):
    def test_cli_returns_nose_joke(self):
        command_line.main()
        out, err = self.capsys.readouterr()
        nose_joke = dog_jokes.what_about_the_nose()
        self.assertTrue(out.__contains__(nose_joke))
        self.assertEqual(err, '')

    # https://github.com/pytest-dev/pytest/issues/2504#issuecomment-309475790
    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys
