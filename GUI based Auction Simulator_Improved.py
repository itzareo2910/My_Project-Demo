import tkinter as tk
from tkinter import messagebox
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# UI Configuration Constants
class UIConfig:
    """Central configuration for UI elements"""
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 650
    TITLE_FONT = ("Arial", 18, "bold")
    LABEL_FONT = ("Arial", 14)
    SUBTITLE_FONT = ("Arial", 12, "italic")
    BUTTON_FONT = ("Arial", 10, "bold")
    SMALL_FONT = ("Arial", 10)
    
    BUDGET_LOW_THRESHOLD = 5000  # Warn when budget is low
    PADDING_X = 20
    PADDING_Y = 20


class Player:
    """Player data class with validation"""
    def __init__(self, name: str, role: str, base: int, experience: str = "Standard"):
        self.name = name
        self.role = role
        self.base = base
        self.experience = experience
    
    def __repr__(self) -> str:
        return f"{self.name} ({self.role})"


class AuctionSimulator:
    """Enhanced Cricket Auction Simulator with improved UX and code organization"""
    
    def __init__(self, root, initial_budget: int = 120000):
        """
        Initialize the auction simulator
        
        Args:
            root: Tkinter root window
            initial_budget: Starting budget for auction
        """
        self.root = root
        self.root.title("🏏 Cricket Auction 2026")
        self.root.geometry(f"{UIConfig.WINDOW_WIDTH}x{UIConfig.WINDOW_HEIGHT}")
        self.root.config(padx=UIConfig.PADDING_X, pady=UIConfig.PADDING_Y)
        
        # Game State Variables
        self.initial_budget = initial_budget
        self.budget = initial_budget
        self.my_squad: List[str] = []
        self.current_player_index = 0
        self.sold_players: List[str] = []
        self.skipped_players: List[str] = []
        self.purchase_history: List[Dict] = []
        
        # Initialize player data
        self.players = self._initialize_players()
        self.total_players = len(self.players)
        
        # Create UI
        self._create_ui()
        
        # Load first player
        self.load_player()
        logger.info(f"Auction started with budget: ₹{self.initial_budget:,}")
    
    @staticmethod
    def _initialize_players() -> List[Player]:
        """Initialize player data with enhanced attributes"""
        return [
            Player("Player A", "Wicket-keeper", 1000, "Experienced"),
            Player("Player B", "Batter", 2000, "Experienced"),
            Player("Player C", "Pacer", 1500, "Standard"),
            Player("Player D", "All-Rounder", 2500, "Experienced"),
            Player("Player E", "Batter", 3000, "Experienced"),
            Player("Player F", "Spinner", 750, "Junior")
        ]
    
    def _create_ui(self) -> None:
        """Create all UI elements"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="🏏 Live Auction", 
            font=UIConfig.TITLE_FONT
        )
        title_label.pack(pady=10)
        
        # Player Counter
        self.counter_label = tk.Label(
            self.root,
            text=f"Player 0 of {self.total_players}",
            font=UIConfig.SMALL_FONT,
            fg="gray"
        )
        self.counter_label.pack(pady=5)
        
        # Player Name
        self.player_label = tk.Label(
            self.root,
            text="Loading...",
            font=UIConfig.LABEL_FONT,
            fg="darkblue",
            wraplength=400
        )
        self.player_label.pack(pady=10)
        
        # Player Details (Role, Base Price, Experience)
        self.role_label = tk.Label(
            self.root,
            text="Loading...",
            font=UIConfig.SUBTITLE_FONT
        )
        self.role_label.pack(pady=5)
        
        # Budget Display
        self.budget_label = tk.Label(
            self.root,
            text=f"Budget: ₹{self.budget:,}",
            font=UIConfig.LABEL_FONT,
            fg="green"
        )
        self.budget_label.pack(pady=15)
        
        # Bid Entry Frame
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)
        
        tk.Label(entry_frame, text="Your Bid:", font=UIConfig.SMALL_FONT).pack(side=tk.LEFT, padx=5)
        self.bid_entry = tk.Entry(
            entry_frame,
            font=UIConfig.LABEL_FONT,
            width=10,
            justify="center"
        )
        self.bid_entry.pack(side=tk.LEFT, padx=5)
        self.bid_entry.bind("<Return>", lambda e: self.process_bid())  # Allow Enter key
        
        # Button Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.bid_button = tk.Button(
            button_frame,
            text="✓ Submit Bid",
            command=self.process_bid,
            bg="green",
            fg="white",
            font=UIConfig.BUTTON_FONT,
            width=12
        )
        self.bid_button.pack(side=tk.LEFT, padx=5)
        
        self.skip_button = tk.Button(
            button_frame,
            text="✗ Skip Player",
            command=self.skip_player,
            bg="orange",
            fg="white",
            font=UIConfig.BUTTON_FONT,
            width=12
        )
        self.skip_button.pack(side=tk.LEFT, padx=5)
        
        # Squad Display
        self.squad_label = tk.Label(
            self.root,
            text="Your Squad: None yet",
            wraplength=420,
            font=UIConfig.SMALL_FONT,
            bg="lightblue",
            padx=10,
            pady=10
        )
        self.squad_label.pack(pady=15, fill=tk.BOTH)
        
        # Stats Frame
        stats_frame = tk.Frame(self.root)
        stats_frame.pack(pady=10, fill=tk.BOTH)
        
        self.stats_label = tk.Label(
            stats_frame,
            text="Sold: 0 | Skipped: 0",
            font=UIConfig.SMALL_FONT,
            fg="gray"
        )
        self.stats_label.pack()
    
    def load_player(self) -> None:
        """Load and display current player's details"""
        if self.current_player_index < self.total_players:
            player = self.players[self.current_player_index]
            
            # Update counter
            self.counter_label.config(
                text=f"Player {self.current_player_index + 1} of {self.total_players}"
            )
            
            # Update player info
            self.player_label.config(text=f"🎯 {player.name}")
            self.role_label.config(
                text=f"Role: {player.role} | Experience: {player.experience}\nBase Price: ₹{player.base:,}"
            )
            
            # Clear previous bid
            self.bid_entry.delete(0, tk.END)
            self.bid_entry.focus()
            
            logger.info(f"Loading player: {player.name} (Base: ₹{player.base})")
        else:
            self.end_auction()
    
    def _validate_bid(self, bid_amount: int) -> tuple[bool, str]:
        """
        Validate the bid amount
        
        Args:
            bid_amount: The bid amount to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        player = self.players[self.current_player_index]
        base = player.base
        
        if bid_amount < base:
            return False, f"Bid must be at least ₹{base:,} (base price)"
        
        if bid_amount > self.budget:
            return False, f"Insufficient budget! You only have ₹{self.budget:,}"
        
        return True, ""
    
    def process_bid(self) -> None:
        """Process the user's bid with enhanced validation"""
        # Get and validate input
        bid_text = self.bid_entry.get().strip()
        
        if not bid_text:
            messagebox.showwarning("Empty Input", "Please enter a bid amount")
            return
        
        try:
            bid_amount = int(bid_text)
            if bid_amount < 0:
                raise ValueError("Bid cannot be negative")
        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Please enter a valid number. {str(e)}")
            return
        
        # Validate bid
        is_valid, error_message = self._validate_bid(bid_amount)
        if not is_valid:
            messagebox.showwarning("Invalid Bid", error_message)
            return
        
        # Process successful bid
        player = self.players[self.current_player_index]
        self.budget -= bid_amount
        self.my_squad.append(player.name)
        self.sold_players.append(player.name)
        self.purchase_history.append({
            "player": player.name,
            "bid": bid_amount,
            "index": self.current_player_index
        })
        
        logger.info(f"Sold {player.name} for ₹{bid_amount}. Remaining budget: ₹{self.budget:,}")
        messagebox.showinfo("✓ Sold!", f"{player.name} bought for ₹{bid_amount:,}!\nRemaining Budget: ₹{self.budget:,}")
        
        self.update_ui()
        self.next_player()
    
    def skip_player(self) -> None:
        """Skip the current player"""
        player = self.players[self.current_player_index]
        self.skipped_players.append(player.name)
        logger.info(f"Skipped: {player.name}")
        self.next_player()
    
    def next_player(self) -> None:
        """Move to the next player"""
        self.current_player_index += 1
        self.load_player()
    
    def update_ui(self) -> None:
        """Update UI with current game state"""
        # Update budget with color coding
        budget_color = "darkred" if self.budget < UIConfig.BUDGET_LOW_THRESHOLD else "green"
        self.budget_label.config(
            text=f"Budget: ₹{self.budget:,}",
            fg=budget_color
        )
        
        # Update squad display
        if self.my_squad:
            squad_text = "Your Squad:\n" + ", ".join(self.my_squad)
        else:
            squad_text = "Your Squad: None yet"
        
        self.squad_label.config(text=squad_text)
        
        # Update stats
        self.stats_label.config(
            text=f"Sold: {len(self.sold_players)} | Skipped: {len(self.skipped_players)}"
        )
    
    def end_auction(self) -> None:
        """Display auction completion and final stats"""
        self.player_label.config(
            text="🎉 Auction Complete!",
            fg="darkgreen",
            font=UIConfig.LABEL_FONT
        )
        self.role_label.config(text="Thank you for playing!")
        
        # Disable inputs
        self.bid_entry.config(state="disabled")
        self.bid_button.config(state="disabled")
        self.skip_button.config(state="disabled")
        
        # Display final summary
        total_spent = self.initial_budget - self.budget
        remaining = self.budget
        
        summary = f"""
        AUCTION SUMMARY
        ━━━━━━━━━━━━━━━━
        Total Players: {self.total_players}
        Players Sold: {len(self.sold_players)}
        Players Skipped: {len(self.skipped_players)}
        
        Initial Budget: ₹{self.initial_budget:,}
        Total Spent: ₹{total_spent:,}
        Remaining: ₹{remaining:,}
        """
        
        messagebox.showinfo("Auction Summary", summary)
        logger.info(f"Auction completed. Final budget: ₹{remaining:,}, Squad size: {len(self.my_squad)}")


def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = AuctionSimulator(root, initial_budget=120000)
    root.mainloop()


if __name__ == "__main__":
    main()
