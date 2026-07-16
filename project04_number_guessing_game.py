print("===== Number Guessing Game =====")
import random
secret_number = random.randint(1, 10)
guess = int(input("Guess the number (1-10): "))
if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number was {secret_number}. Better luck next time!")
    print("correct number was", secret_number)
if guess == secret_number:
    print("You Win! 🏆")
else:
    print("You Lose! 😢")
