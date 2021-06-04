import sys
from mypypackage.funnies import dog_jokes
from mypypackage.funnies import cat_jokes

help_message = "tellmeajoke [DOG|CAT]"

def main() -> None:
  if len(sys.argv) > 1:
    if sys.argv[1].lower() == 'dog':
        print(dog_jokes.get_joke())
        return
    if sys.argv[1].lower() == 'cat':
        print(cat_jokes.get_joke())
        return
  print(help_message)

if __name__ == '__main__':
  main()
