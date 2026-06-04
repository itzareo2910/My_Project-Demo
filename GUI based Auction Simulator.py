import tkinter as tk
from tkinter import messagebox

class AuctionSimulator:
    def __init__(self, root):
        # 1. Setup the main window
        self.root = root
        self.root.title("Cricket Auction 2026")
        self.root.geometry("450x450")
        self.root.config(padx=20, pady=20)

        # 2. Game Variables (State)
        self.budget = 120000
        self.my_squad = []
        self.current_player_index = 0 # Tracks which player is currently on the block
        
        self.players = [
            {"name": "Player A", "role": "Wicket-keeper", "base": 1000},
            {"name": "Player B", "role": "Batter", "base": 2000},
            {"name": "Player C", "role": "Pacer", "base": 1500},
            {"name": "Player D", "role": "All-Rounder", "base": 2500},
            {"name": "Player E", "role": "Batter", "base": 3000},
            {"name": "Player F", "role": "Spinner", "base": 750}
        ]

        # 3. Create the UI Elements (Labels, Entry, Buttons)
        self.title_label = tk.Label(root, text="Live Auction", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        self.player_label = tk.Label(root, text="Loading...", font=("Arial", 14))
        self.player_label.pack(pady=5)

        self.role_label = tk.Label(root, text="Loading...", font=("Arial", 12, "italic"))
        self.role_label.pack(pady=5)

        self.budget_label = tk.Label(root, text=f"Budget: {self.budget}", font=("Arial", 14, "bold"), fg="green")
        self.budget_label.pack(pady=15)

        # Input box for bidding
        self.bid_entry = tk.Entry(root, font=("Arial", 14), width=10, justify="center")
        self.bid_entry.pack(pady=10)

        # Buttons
        self.bid_button = tk.Button(root, text="Submit Bid", command=self.process_bid, bg="blue", fg="white", font=("Arial", 12, "bold"))
        self.bid_button.pack(pady=5)

        self.skip_button = tk.Button(root, text="Skip Player", command=self.skip_player, font=("Arial", 10))
        self.skip_button.pack(pady=5)

        self.squad_label = tk.Label(root, text="Your Squad: []", wraplength=400, font=("Arial", 10))
        self.squad_label.pack(pady=20)

        # 4. Start the game by loading the first player
        self.load_player()

    def load_player(self):
        """Updates the screen with the current player's details."""
        if self.current_player_index < len(self.players):
            player = self.players[self.current_player_index]
            self.player_label.config(text=f"Up for auction: {player['name']}")
            self.role_label.config(text=f"Role: {player['role']} | Base Price: {player['base']}")
            self.bid_entry.delete(0, tk.END) # Clear the text box
        else:
            self.end_auction()

    def process_bid(self):
        """Runs when the user clicks 'Submit Bid'."""
        try:
            bid_amount = int(self.bid_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers only.")
            return

        player = self.players[self.current_player_index]
        base = player["base"]

        # Check if the bid is valid
        if bid_amount >= base and bid_amount <= self.budget:
            self.budget -= bid_amount
            self.my_squad.append(player["name"])
            messagebox.showinfo("Sold!", f"{player['name']} bought for {bid_amount}!")
            self.update_ui()
            self.next_player()
        else:
            messagebox.showwarning("Invalid Bid", "You either bid below the base price or don't have enough budget!")

    def skip_player(self):
        """Runs when the user clicks 'Skip Player'."""
        self.next_player()

    def next_player(self):
        """Moves the index forward and loads the next player."""
        self.current_player_index += 1
        self.load_player()

    def update_ui(self):
        """Updates the budget and squad lists on the screen."""
        self.budget_label.config(text=f"Budget: {self.budget}")
        self.squad_label.config(text=f"Your Squad: {', '.join(self.my_squad)}")

    def end_auction(self):
        """Disables the inputs when the auction is over."""
        self.player_label.config(text="Auction Complete!", font=("Arial", 16, "bold"), fg="red")
        self.role_label.config(text="Thank you for playing.")
        self.bid_entry.config(state="disabled")
        self.bid_button.config(state="disabled")
        self.skip_button.config(state="disabled")

# 5. Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = AuctionSimulator(root)
    root.mainloop()