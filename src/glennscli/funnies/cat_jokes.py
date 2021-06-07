import random

jokes = [
    'Why did the cats ask for a drum set? They wanted to make some mewsic!',
    'What\'s a cat\'s favorite TV show? Claw and Order!',
    'What normally happens when kitties go on a first date? They hiss!',
    'What\'s a cat\'s favorite cereal? Mice crispies!'
]


def get_jokes(numjokes):
    if numjokes > len(jokes):
        return random.sample(jokes, len(jokes))
    if numjokes <= 0:
        return random.sample(jokes, 1)

    return random.sample(jokes, k=numjokes)
