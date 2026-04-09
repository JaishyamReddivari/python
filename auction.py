import os

print("Welcome to the secret auction program")
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
more = input("Are there any other bidders? Type 'yes' or 'no'.\n")

bids = {}
bids[name] = bid

while more == "yes":
    os.system('clear')
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bids[name] = bid

print(bids)

max_bid = max(bids.values())
for key, value in bids.items():
    if value == max_bid:
        print(f"The winner is {key} with a bid of ${max_bid}.")
