import random
import math
import time
import os
import json
from unittest import result
score = 0

def wordle_load_dictionary(file_path):
    with open(file_path) as f:
        
        words = [line.strip().lower() for line in f]
    return words

def wordle_is_valid_guess(guess, guesses):
    return guess in guesses

def poople_is_valid_word(word, words):
    return word in words



def wordle_evaluate_guess(guess, word):

    guess = guess.lower()
    word = word.lower()
    
    result = ["Grey"] * 5
    word_chars = list(word)

    for i in range(5):
        if guess[i] == word_chars[i]:
            result[i] = "Green"
            word_chars[i] = None 


    for i in range(5):
        if result[i] == "Green":
            continue
        if guess[i] in word_chars:
            result[i] = "Yellow"

            word_chars[word_chars.index(guess[i])] = None


    return " ".join(result)




def wordle(wordle_guesses, wordle_answers):


    global score
    time.sleep(1)
    print("Wordle!")
    time.sleep(0.2)
    print("In this game, you will have to guess a secret five-letter word.")
    print("You have 6 tries to guess the word.")
    time.sleep(0.2)
    print("After each guess, you will receive feedback on your guess with colors")
    time.sleep(0.2)
    print("Grey letters are not in the word;")
    time.sleep(0.2)
    print("Yellow letters are in the word but in the wrong position;")
    time.sleep(0.2)
    print("Green letters are in the correct position.")
    time.sleep(0.2)
    print("You will earn points based on how many attempts it takes you to guess the word.")
    time.sleep(0.2)
    print("Type 'exitt' to leave")
    time.sleep(0.2)
    print("Good luck!")
    time.sleep(0.5)

    secret_word = random.choice(wordle_answers)
    attempts = 1
    max_attempts = 6
    wordle_points = 0

    while attempts <= max_attempts:
        time.sleep(0.5)
        guess = input(f"Attempt {attempts}/{max_attempts}: ").lower()
        if guess == "exitt":
            print("You have chosen to exit the game.")
            time.sleep(0.2)
            wordle_points = 0
            break
        if not wordle_is_valid_guess(guess, wordle_guesses):
            print("Invalid guess. Please try again.")
            time.sleep(0.2)
            continue

        result = wordle_evaluate_guess(guess, secret_word)
        print(result)
        time.sleep(0.2)




        if guess == secret_word:
            print(f"Congratulations! You've guessed the word '{secret_word}' in {attempts} attempts.")
            time.sleep(0.2)

            if attempts == 1:
                wordle_points = 200
            elif attempts == 6:
                wordle_points = 10
            else:
               wordle_points = round(( (max_attempts - attempts) / (max_attempts - 1) ) * 200)


            score += wordle_points
            time.sleep(1)
            break

        attempts += 1
        if attempts > max_attempts:
            print(f"Sorry, you've used all your attempts. The secret word was '{secret_word}'.")
            time.sleep(0.2)
            wordle_points = 0
            score += wordle_points
            time.sleep(1)
            break
    return wordle_points


def poople(poople_words):
  global score
  time.sleep(1)
  print("Poople!")
  time.sleep(0.2)
  print("Welcome to Poople!")
  time.sleep(0.2)
  print("In this game, you will be given a random four letter word.")
  time.sleep(0.2)
  print("Each turn, you can modify one letter of the word to create a new four letter word.")
  time.sleep(0.2)
  print("You need to change the word to Poop in as few turns as possible.")
  time.sleep(0.2)
  print("You will earn points based on how many turns it takes you to reach Poop.")
  time.sleep(0.2)
  print("Type 'exitt' to leave.")
  time.sleep(0.2)
  print("Good luck!")
  time.sleep(0.5)

  poople_points = 0
  p_attempts = 0
  p_max_attempts = 25
  current_word = random.choice(poople_words)
  print("Your starting word is:", current_word)
  time.sleep(0.2)

  while p_attempts < p_max_attempts:
    time.sleep(0.5)
    new_word = input(
        f"Attempt {p_attempts + 1}/{p_max_attempts}: The current word is {current_word}. Enter a new four-letter"
        " word by changing one letter: "
    ).lower()
    
    if new_word == "exitt":
      print("You have chosen to exit the game.")
      time.sleep(0.2)
      poople_points = 0
      break

    if len(new_word) != 4:
      print("Invalid input. Please enter a four-letter word.")
      time.sleep(0.2)
      continue

    if not poople_is_valid_word(new_word, poople_words):
      print("Invalid word. Please try again.")
      time.sleep(0.2)
      continue

    if sum(1 for a, b in zip(current_word, new_word) if a != b) != 1:
      print("You can only change one letter at a time. Please try again.")
      time.sleep(0.2)
      continue

    current_word = new_word
    p_attempts += 1

    if current_word == "poop":
      time.sleep(0.2)
      print(
          f"Congratulations! You've transformed the word to Poop in"
          f" {p_attempts} attempts.")
      time.sleep(0.2)
      if p_attempts == 1:
        poople_points = 200
      elif p_attempts == 25:
        poople_points = 10
      else:
        poople_points = round(((p_max_attempts - p_attempts) / (p_max_attempts - 2)) * 150)
      time.sleep(0.5)
      break
    if p_attempts >= p_max_attempts:
        print("Sorry, you've used all your attempts. Better luck next time!")
        time.sleep(0.5)
        poople_points = 0
        break

  score += poople_points
  return poople_points


def num_guessing():
    global score
    time.sleep(1)
    print("Number guessing game!")
    time.sleep(0.2)
    print("You will have to guess a random number between 1-1000 in under 20 attempts.")
    time.sleep(0.2)
    print("You will know if it it is lower or higher than your guess.")
    time.sleep(0.2)
    print("Type '12345' to leave")
    time.sleep(0.2)
    print("Good luck.")
    time.sleep(0.5)
    guess_number = random.randint(1,1000)
    max_guesses = 20
    guesses_count = 0
    number_points = 0
    guessed_numbers = []



    while guesses_count < max_guesses:
        time.sleep(0.2)
        print(f"I have chosen a random number from 1-1000. Take a guess. Attempts: {guesses_count}/{max_guesses}")
        time.sleep(0.2)
        user_input = input("Guess a number: ")
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid guess. Try again.")
            time.sleep(0.2)
            continue

        if guess == 12345:
            print("You have chosen to exit the game.")
            time.sleep(0.2)
            number_points = 0
            break

        if guess in guessed_numbers:
            print("Sorry, you guessed that number already. Try again.")
            time.sleep(0.2)
            continue
        guessed_numbers.append(guess)
        if (guess > guess_number):
            print("That's too high. Try again.")
            time.sleep(0.2)
            guesses_count += 1
            continue
        if (guess < guess_number):
            print("That's too low. Try again.")
            time.sleep(0.2)
            guesses_count += 1
            continue
        if guess == guess_number:
            guesses_count += 1
            print(f"Congrats! You guessed the secret number {guess_number} in {guesses_count} guesses.")
            time.sleep(0.2)
            number_points = round(((max_guesses - guesses_count) / max_guesses) *150)
            time.sleep(0.5)
            break

    if guesses_count >= max_guesses:
        print(f"Sorry, you're out of guesses. The number was {guess_number}")
        time.sleep(0.2)
        number_points = 0

    score += number_points
    time.sleep(0.2)
    return number_points


def rps_game():
    time.sleep(1)
    print("Rock Paper Scissors!")
    time.sleep(.2)
    print("You will be playing rock paper scissors with me.")
    time.sleep(.2)
    print("We will be playing 5 rounds, and you get points for how many wins you get")
    time.sleep(.2)
    print("Type 'exitt' to leave")
    time.sleeo(0.2)
    print("Good luck.")
    time.sleep(0.5)

    rounds = 0
    wins = 0
    max_rounds = 5
    rps_points = 0

    while rounds <= max_rounds:
        time.sleep(.5)
        choice = input("Type rock, paper, or scissors.")
        if choice == "exitt":
            print("You have chosen to leave.")
            time.sleep(0.2)
            rps_points = 0
            break
    
        if choice != "rock" or "paper" or "scissors":
            print("Invalid guess. Try again")
            time.sleep(0.2)
            continue
        ai_choice = random.choice["rock", "paper", "scissors"]

        print(f"Your choice was {choice} and mine was {ai_choice}.")

        if choice == ai_choice:
            print("We drawed.")
            wins += 0.5
            rounds += 1
            continue
        if choice == "rock" and ai_choice == "scissors":
            print("You won.")
            wins += 1
            rounds += 1
            continue
        if choice == "paper" and ai_choice == "rock":
            print("You won.")
            wins += 1
            rounds += 1
            continue
        if choice == "scissors" and ai_choice == "paper":
            print("You won.")
            wins += 1
            rounds += 1
            continue
        # if you los
        if choice == "rock" and ai_choice == "paper":
            print("You lost.")
            rounds += 1
            continue
        if choice == "paper" and ai_choice == "scissors":
            print("You lost.")
            rounds += 1
            continue
        if choice == "scissors" and ai_choice == "rock":
            print("You lost.")
            rounds += 1
            continue
    if rounds > max_rounds:
        print("Okay, your time is up now!")
        print(f"Looks like you won {wins} amount of times.")
        rps_points = round(((max_rounds - wins) / max_rounds) * 150)
        print(f"Your score from this round is {rps_points}")
    score += rps_points
    return rps_points
            
# ssouhukshksnsknjksnds




def hangman(hangman_words):
    time.sleep(1)
    global score
    print("Hangman!")
    time.sleep(0.2)
    print("Welcome to Hangman!")
    time.sleep(0.2)
    print("In this game, you will have to guess a secret word by guessing letters.")
    time.sleep(.2)
    print("You gain one body part for each incorrect guess, and you have a maximum of 6 incorrect guesses before you lose.")
    time.sleep(0.2)
    print("You will earn points based on how many guesses you take.")
    time.sleep(.2)
    print("Type 'exitt' to leave.")
    time.sleep(.2)
    print("Good luck!")
    time.sleep(.5)

    secret_word = random.choice(hangman_words)
    guessed_letters = set()
    attempts = 0
    max_attempts = 6
    hangman_points = 0

    while attempts < max_attempts:
        time.sleep(0.5)
        display_word = "".join(
            [letter if letter in guessed_letters else "_" for letter in secret_word]
        )
        print(f"Word: {display_word}")
        guess = input("Guess a letter: ").lower()
        time.sleep(0.2)

        if guess == "exitt":
            print("You have chosen to exit the game.")
            time.sleep(0.2)
            hangman_points = 0
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            time.sleep(.2)
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            time.sleep(.2)
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            time.sleep(0.2)
        else:
            attempts += 1
            print(f"Sorry, '{guess}' is not in the word. Attempts: {attempts}/{max_attempts}")
            time.sleep(0.2)

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You've guessed the word '{secret_word}' with {attempts} attempts.")
            time.sleep(0.2)
            hangman_points = round(((max_attempts - attempts) / max_attempts) * 150)
            break

    if attempts >= max_attempts:
        time.sleep(0.2)
        print(f"Sorry, you've used all your attempts. The secret word was '{secret_word}'.")
        hangman_points = 0

    score += hangman_points
    return hangman_points


FILE_NAME = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_score(player,score):
    data = load_leaderboard()
    if player not in data or score > data[player]:
        data[player] = score
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)



def display_top_leaderboard(top_n=5):
    data = load_leaderboard()
    sorted_lb = sorted(data.items(), key=lambda x: x[1], reverse=True)

    print(f"\n--- Top {top_n} Leaderboard ---")
    for rank, (player, score) in enumerate(sorted_lb[:top_n], start=1):
        print(f"{rank}. {player} - {score}")


def calculator():
    print("Welcome to my calculator app!")
    print("Enter the first digit")
    first = int(input())
    print("Now enter the math you want to do (type '+', '-', 'x', or '/')")
    symbol = input()
    print("Now enter the second digit")
    second = int(input())
    print(f"Your equation is {first} {symbol} {second}")

    if symbol == "+":
        math_answer = first + second
    if symbol == "-":
        math_answer = first - second
    if symbol == "x":
        math_answer = first * second
    if symbol == "/":
        math_answer = first / second

    print(f"Your result is {math_answer}.")








#
#
#
# Code here


def main():


    print("Welcome to the Omnidle!")
    time.sleep(0.2)
    print("In this game, you will go through a gauntlet of games, and your score will be tracked across all of them.")
    time.sleep(0.2)
    print("First, please enter your name:")
    username = input()
    time.sleep(0.2)
    print(f"Okay, {username}, want to see the leaderboard? (yes/no)")
    response = input().lower()
    if response == "yes":
        display_top_leaderboard()
    time.sleep(0.2)
    print(f"Now, {username}! Let's begin Omnidle!")
    time.sleep(0.2)
    print("The first game will be...")
    time.sleep(0.5)
    
    global score
    score = 0




    the_wordle_guesses = wordle_load_dictionary("wordle_guesses.txt")
    the_wordle_answers = wordle_load_dictionary("wordle_answers.txt")
    wordle_points_earned = wordle(the_wordle_guesses, the_wordle_answers)
    time.sleep(0.5)
    print("Your current score is:", score, "points.")
    time.sleep(0.2)
    print("You gained", wordle_points_earned, "points from this game.")
    time.sleep(0.5)

    print("Congrats! You have completed the first game of Omnidle!")
    time.sleep(0.2)
    print("The next game will be...")
    time.sleep(0.5)

    poople_words = wordle_load_dictionary("poople_words.txt")
    poople_points_earned = poople(poople_words)
    time.sleep(0.5)
    print("Your current score is:", score, "points.")
    time.sleep(0.2)
    print("You gained", poople_points_earned, "points from this game.")
    time.sleep(0.5)

    print("Congrats! You have completed the second game of Omnidle!")
    time.sleep(0.2)
    print("The next game will be...")
    time.sleep(0.5)

    hangman_words = wordle_load_dictionary("hangman_words.txt")
    hangman_points_earned = hangman(hangman_words)
    time.sleep(0.5)
    print("Your current score is:", score, "points.")
    time.sleep(0.2)
    print("You gained", hangman_points_earned, "points.")
    time.sleep(0.5)
    
    print("Congrats! You have completed the third game of Omnidle.")
    time.sleep(0.2)
    print("The next game will be...")
    time.sleep(0.5)

    number_points_earned = num_guessing()
    time.sleep(0.5)
    print("Your current score is:", score, "points.")
    time.sleep(0.2)
    print("You gained", number_points_earned, "points.")
    time.sleep(0.5)

    print("Congrats! You have completed the fourth game of Omnidle.")
    time.sleep(0.2)
    print("The next game will be...")
    time.sleep(0.5)
    rps_points_earned = rps_game()
    time.sleep(0.5)
    print("Your current score is", score, "points.")
    time.sleep(0.2)
    print("You gained", rps_points_earned, "points.")

   

    print("Congrats! You have completed the last game of Omnidle!")
    time.sleep(0.2)
    print("Your final score is:", score, "points.")
    time.sleep(0.5)
    save_score(username, score)
    print("Your score has been saved to the leaderboard.")
    time.sleep(0.2)
    print("Would you like to view it? (yes/no)")
    response = input().lower()
    if response == "yes":
        display_top_leaderboard()


    time.sleep(0.5)
    print("Would you like to play again? (yes/no)")
    response = input().lower()
    if response == "yes":
        main()
    if response == "no":
        print("Okay buddy... Thanks for playing Omnidle!")


main()

time.sleep(0.2)
print("You have ended the program. Thanks for playing")
time.sleep(3)
print("End the program please. Have a great day")
time.sleep(60)

print("Please end it pretty please")

def wordle_test():
    global score
    print("welcome to wordle")
    print("this is a game")
    print("ive veeb working so i hope i get a for ours ad hours")