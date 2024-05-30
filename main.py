import random

def play_game():
  """
  A simple guessing game.
  """
  number = random.randint(1,5)
  guesses = 0
  while True:
    try:
      guess = int(input("Guess a number between 1 and 5: "))
      guesses += 1
      if guess < number:
        print("Too low! Guess again.")
      elif guess > number:
        print("Too high! Guess again.")
      else:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        with open("ascii_art.txt", "r") as f:
          ascii_art = f.read()
          print(ascii_art)
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  play_game()