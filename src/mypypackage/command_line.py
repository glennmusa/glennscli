import sys
from mypypackage.funnies import dog_jokes
from mypypackage.funnies import cat_jokes

help_message = "tellmeajoke [DOG|CAT]"

def main() -> None:
  if len(sys.argv) > 1:
    if sys.argv[1].lower() == 'dog':
        print(dog_jokes.what_about_the_nose())
        return
    if sys.argv[1].lower() == 'cat':
        print(cat_jokes.whats_their_favorite_show())
        return
  print(help_message)
