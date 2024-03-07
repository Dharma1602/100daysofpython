## Black Jack Game
import os
import random
from art import logo
def deal_card():
   """Returns a random card from the deck"""
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card
   

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Loose, computer has BlackJack"
    elif user_score == 0:
        return "You WON with a Blackjack"
    elif user_score > 21:
        return "You went over 21, You Loose"
    elif computer_score > 21:
        return "Opponent went over 21, You Win"
    elif user_score > computer_score:
        return " You Win"
    else:
        return "You loose"
def play_game():
    user_card = []
    computer_card = []
    is_game_over = False
    print(logo)

    for i in range(2):
        # new_card = deal_card()
        # user_card.append(new_card)
        user_card.append(deal_card())
        computer_card.append(deal_card())



    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"the user cards are {user_card} and current score is {user_score}")
        print(f"the computer first card is  {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card or 'n' to end.")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f" Your final hand is: {user_card} and final score is {user_score}")
    print(f"Computer final hand is {computer_card} and final score is {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score))

while input("Do you want to play a game of Blackjack: type y or n: ") == "y":
    os.system('cls')
    play_game()