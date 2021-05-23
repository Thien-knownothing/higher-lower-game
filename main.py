from art import logo, vs
from game_data import data
from replit import clear
import random

#This is a game to compare instagram follower, you will fight again computer to guess the provided instagram by computer have higher or lower compare to your provided once

def selection(data):
  """
  This function will generate random Instagram account base in data from game_data and remove the data that being generated from selection pool. 
  """
  select = random.choice(data)
  print(f"Instagram: {select['name']}, a {select['description']}, from {select['country']}")
  data.remove(select)
  return select,data


def check_win(computer,player):
  """
  This function will take in player and computer selected account and make player guess the lower or the higher of their account's follower compared to computer's
  The 2 argument being passed in this function is 2 tubes since selection() function is assigned to these parameter and it return 2 parameter(select,data)

  """
  player_guess = input("Guess if your Instagram follower is higher or lower than computer's once: ")
  if player_guess[0].lower() == "h":
    if computer[0]['follower_count'] > player[0]['follower_count']:
      #computer[0] mean to be selection(data)[0] which is selection(data)'s select which is random.choice(data)
      print("you lose")
      return False
    else:
      print("you get it right")
      return True
      
  if player_guess[0].lower() == "l":
    if computer[0]['follower_count'] < player[0]['follower_count']:
      print("you lose")
      return False
    else:
      print("you get it right")
      return True



      
game_on = True  
score = 0
while game_on:
  print(logo)
  computer = selection(data)
  print(vs)
  player = selection(data) 
  check = check_win(computer,player)
  if check == True:
    score += 1
    clear()
    print(f'You get it right, your current score is {score}')
  else:
    print(f"Your score is {score}")
    cont = input("Do you want to continue? Yes/No ")
    if cont[0].lower() == "y":
      score = 0
      clear()
    else:
      print("thanks for play")
      game_on = False





