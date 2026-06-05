budget = 120000
my_squad = []

# Structured the players as a list of dictionaries for easy access
players = [
    {"name": "Player A", "role": "Wicket-keeper", "base": 1000},
    {"name": "Player B", "role": "Batter", "base": 2000},
    {"name": "Player C", "role": "Pacer", "base": 1500},
    {"name": "Player D", "role": "All-Rounder", "base": 2500},
    {"name": "Player E", "role": "Batter", "base": 3000},
    {"name": "Player F", "role": "Spinner", "base": 750},
    {"name": "Player G", "role": "Pacer", "base": 1000},
    {"name": "Player H", "role": "All-Rounder", "base": 3000}
]

for player in players:
    base = player["base"]
    name = player["name"]
    role = player["role"]
    
    print(f"--- Up for auction: {name} ---")
    print(f"Role: {role} | Base Price: {base}")
    print(f"Total Budget Remaining: {budget}")
    
    # Capture the user's input
    try:
        bid_amount = int(input("Enter your bid amount (Enter 0 to skip): "))
    except ValueError:
        print("Invalid input. Please enter numbers only. Player skipped.")
        print("\n")
        continue # Skips to the next player if they type a letter by mistake
    
    # Check the bid logic
    if bid_amount == 0:
        print(f"{name} skipped.")
    elif bid_amount >= base and bid_amount <= budget:
        budget -= bid_amount
        # Adding just the player's name to the squad list for cleaner output
        my_squad.append(name) 
        print(f"{name} bought for {bid_amount}!")
    else:
        print("Invalid bid. You either bid below the base price or don't have enough budget. Skipped.")
        
    print("\n") # Adds a blank line for readability between players

print("========== Auction Complete! ==========")
print("Your Squad:", my_squad)
print("Remaining Budget:", budget)