import random

joke_list = [
    "Why don't programmers like nature? It has too many bugs.",
    "Why do Java developers wear glasses? Because they don't C#.",
    "Debugging: Being the detective in a crime movie where you're also the murderer."
]

def get_random_joke():
    return random.choice(joke_list)
