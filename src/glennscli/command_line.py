import sys

from knack import CLI
from knack.commands import CLICommandsLoader, CommandGroup
from knack.arguments import ArgumentsContext

from glennscli.funnies import dog_jokes
from glennscli.funnies import cat_jokes


def tellmeajoke_dog(numjokes=1):
    return dog_jokes.get_jokes(numjokes)


def tellmeajoke_cat(numjokes=1):
    return cat_jokes.get_jokes(numjokes)


class MyCommandsLoader(CLICommandsLoader):

    def load_command_table(self, args):
        with CommandGroup(self, 'tellmeajoke', 'glennscli.command_line#{}') as g:
            g.command('dog', 'tellmeajoke_dog')
            g.command('cat', 'tellmeajoke_cat')
        return super(MyCommandsLoader, self).load_command_table(args)

    def load_arguments(self, command):
        with ArgumentsContext(self, 'tellmeajoke dog') as ac:
            ac.argument('numjokes', type=int)
        with ArgumentsContext(self, 'tellmeajoke cat') as ac:
            ac.argument('numjokes', type=int)
        super(MyCommandsLoader, self).load_arguments(command)


cli_name = "glennscli"


def my_cli():
    return CLI(cli_name=cli_name, commands_loader_cls=MyCommandsLoader)


def main():
    cli = my_cli()
    exit_code = cli.invoke(sys.argv[1:])
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
