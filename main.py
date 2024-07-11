import art
import game_data
import random
from replit import clear
score = 0

def compare(name_1, name_2):
  global highest_followers
  highest_followers = max(name_1["follower_count"], name_2["follower_count"])
  game(name_1, name_2)

def check_answer(answer, name_A, name_B):
  global score
  global highest_followers
  if answer == "A":
    if name_A["follower_count"] == highest_followers:
      clear()
      score += 1
      print(f"You are right! Current score: {score}.")
      name_A = name_B
      name_B = random.choice(game_data.data)
      compare(name_A, name_B)
    else:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}.")
  elif answer == "B":
    if name_B["follower_count"] == highest_followers:
      clear()
      score += 1
      print(f"You are right! Current score: {score}.")
      name_A = name_B
      name_B = random.choice(game_data.data)
      compare(name_A, name_B)
    else:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}.")
  elif answer == "A" or answer == "B":
    if name_A["follower_count"] == name_B["follower_count"]:
      clear()
      print(f"There is a tie in the follower count. Current score: {score}.")
    name_A = name_B
    name_B = random.choice(game_data.data)
    compare(name_A, name_B)
  else:
    clear()
    print(f"Sorry, that's wrong. Final score: {score}.")


def game(name_A, name_B):  
  print(art.logo)
  print(f'Compare A: {(name_A["name"])}, a {(name_A["description"])}, from {(name_A["country"])}.')
  print(art.vs)
  print(f'Against B: {(name_B["name"])}, a {(name_B["description"])}, from {(name_B["country"])}.')
  answer = input("Who has more followers? Type 'A' or 'B':\n").upper()
  check_answer(answer, name_A, name_B)

def start_game():
  name_A = random.choice(game_data.data)
  name_B = random.choice(game_data.data)
  compare(name_A, name_B)
start_game()
