import random

jokes = [
    'My dog has no nose. He smells awful!',
    'What type of markets do dogs avoid? Flea markets!',
    'What breed of dog does Dracula have? A Bloodhound!',
    'How does the dog always know who is calling? He has collar ID!'
]

def get_joke() -> str:
    return random.choice(jokes)

