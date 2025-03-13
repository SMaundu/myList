import random

def random_joke():
    """Displays a random joke about Python or programming."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Python programmers have low self-esteem? Because they're constantly comparing their self to others.",
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why do Java developers wear glasses? Because they don't see sharp."
    ]

    joke = random.choice(jokes)
    print(joke)

if __name__ == "__main__":
    random_joke()