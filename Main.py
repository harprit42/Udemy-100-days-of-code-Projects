############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#a = random.choice(cards)

'''
1. ask user to start playing the game. if user types y, start the game in a while loop.
2. create 2 lists one for the player and other for computer. create a draw card function and draw random card from the deck. - lists and draw_card function created
3. create a function to display the cards - not needed just display the list
4. create a function to sum the cards in the list. use sort and if the sum is more than 21 and there is an ace drawn, optimize the sum. - get_score function created
4. create a validate sum function to check if the sum of the cards in list is 21 or not. add functionality to check the ace card's value.
5. create a function to check winner
'''

def draw_card(list):
  list.append(random.choice(cards))
  return list

def get_score(list):
  score = 0
  list.sort()
  for card in list:
    if card == 11:
      if score > 12:
        card = 1
      else:
        card = 10
    score += card
  return score


keep_playing_flag = 'y'

# START GAME HERE

while keep_playing_flag.lower() == 'y':
  keep_playing_flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
  player_cards = [] 
  dealer_cards = []
  player_cards = draw_card(player_cards)
  player_cards = draw_card(player_cards)
  dealer_cards = draw_card(dealer_cards)
  print(logo)
  player_score = get_score(player_cards)
  dealer_score = get_score(dealer_cards)
  print(f"Your cards: {player_cards}, current score: {player_score}")
  print(f"Computer's first card: {dealer_cards}")
  
  player_hit = 'y'
  while player_score <= 21 and player_hit == 'y':
    player_hit = input("Type 'y' to get another card. Type 'n' to pass: ")
    print(f"Your cards: {player_cards}, current score: {player_score}")
    if player_hit == 'y':
      draw_card(player_cards)
      player_score = get_score(player_cards)
  
  print(f"Your Final Hand: {player_cards}, final score {player_score}")
  
  if player_score > 21:
    print("You went over. You lose")
    keep_playing_flag = 'n'
  
  while dealer_score < player_score:
    draw_card(dealer_cards)
    dealer_score = get_score(dealer_cards)

  print(f"Computer Final Hand {dealer_cards}, final score {dealer_score}")
  
  if dealer_score > 21:
    print("Opponent went over. You win")
    keep_playing_flag = 'n'
  elif dealer_score >= player_score:
    print("You lose")
    keep_playing_flag = 'n'


  
