def personalized_greeting():
  """Asks for user's name and favorite color, then prints a greeting."""

  name = input("What's your name? ")
  color = input("What's your favorite color? ")

  print(f"Hello, {name}! Your favorite color, {color}, is awesome!")

personalized_greeting()