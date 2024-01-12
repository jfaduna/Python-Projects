import os

from art import logo

print("Welcome to the secret auction program")

bidders = {}

def get_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(logo)
    print("SOLD!")
    print(f"The winner is {winner} with a bid of ${highest_bid}! \n")

print(logo)

still_bidding = True
while still_bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == 'no':
        os.system('cls' if os.name == 'nt' else 'clear')
        highest_bidder = get_highest_bidder(bidders)
        still_bidding = False
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
