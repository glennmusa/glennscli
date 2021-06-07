import unittest
from glennscli import command_line
from knack.testsdk import ScenarioTest, JMESPathCheck

class TestJokeScenarios(ScenarioTest):

    def __init__(self, method_name):
        mycli = command_line.my_cli()
        super(TestJokeScenarios, self).__init__(mycli, method_name)

    def test_tellmeajoke_cat(self):
        self.cmd('tellmeajoke cat')

    def test_tellmeajoke_cat_with_numjokes(self):
        self.cmd('tellmeajoke cat --numjokes 3', JMESPathCheck('length(@)', 3))

    def test_tellmeajoke_dog(self):
        self.cmd('tellmeajoke dog')

    def test_tellmeajoke_dog_with_numjokes(self):
        self.cmd('tellmeajoke dog --numjokes 3', JMESPathCheck('length(@)', 3))

if __name__ == '__main__':
    unittest.main()
