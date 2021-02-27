import random
from cmd import Cmd

from colorama import Fore, Style


def _get_color() -> str:
    return random.choice([  # noqa: S311
        Fore.BLUE,
        Fore.CYAN,
        Fore.GREEN,
        Fore.MAGENTA,
        Fore.YELLOW,
        Fore.RED,
    ])


def _hyphens() -> str:
    line = '─' * 100
    return f'{_get_color()}{line}{Style.RESET_ALL}'


def _get_prompt() -> str:
    return f"""
{_hyphens()}

c                   => create new todo
d                   => delete todo
da                  => delete all todos
sa                  => show all todos
sd                  => search by partial description
sid                 => search by id
ud                  => update description
udl                 => update deadline
e | q | exit | quit => exit the application
anything else       => show the main menu

Please enter a command:\n"""


class TodoShell(Cmd):
    """The shell interface."""

    prompt = _get_prompt()

    def postcmd(self, stop, line) -> None:
        print(stop, line)
        self.prompt = _get_prompt()
        return stop

    def do_c(self, arg):
        description = input('Please enter a description: ')
        deadline = input('Please enter a deadline in the following format yyyy-mm-dd H:m: ')
        return False

    def do_e(self, arg):
        return True

    def do_q(self, arg):
        return True

    def do_exit(self, arg):
        return True

    def do_quit(self, arg):
        return True


if __name__ == '__main__':
    TodoShell().cmdloop()
