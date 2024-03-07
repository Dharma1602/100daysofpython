from art import logo

print(logo)


import os

# Clearing the Screen
os.system('cls')


# name = input("Please enter your name: \n")
# bid_price = int(input("Enter your bid: $"))

bids = {}
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}")

other_bidders = True
while other_bidders:
    name = input("Please enter your name: \n")
    bid_price = int(input("Enter your bid: $"))
    bids[name] = bid_price
    os.system('cls')
    # bid(person=name, price=bid_price)
    
    
    result = input("Type 'yes' if there are any other bidders, OR press 'no'")
    if result == "no":
        other_bidders = False
        find_highest_bidder(bids)
        