# Blackjack Game in Python (blackjack-game-py)

## Overview
This project provides a basic implementation of the Blackjack card game in Python. It’s a text-based experience where players compete against a dealer to get as close to 21 as possible without exceeding it. Perfect for beginners learning Python and game development concepts.

---

## Features
- Random card assignment for players and the dealer.
- User input for **"Hit"** (take another card) or **"Stand"** (keep current total).
- Automated dealer gameplay.
- Win, lose, or draw conditions based on Blackjack rules.

---

## How to Play

### Clone the Repository
Run the following command in your terminal to clone the repository:
```bash
git clone https://github.com/<your-username>/simple-blackjack-game.git
```

### Navigate to the Project Folder
Run the `cd` command to move into the project folder:
```bash
cd simple-blackjack-game
```

### Run the Game
Execute the Python script using the following command:
```bash
python blackjack.py
```

This will start the Blackjack game, allowing you to play against the dealer.

---

## Example Output
Here’s an example of what you’ll see while playing:
```plaintext
Your cards: [5, 10], current score: 15
Dealer's first card: 8
Type 'y' to get another card, type 'n' to pass: y
Your cards: [5, 10, 3], current score: 18
Dealer's cards: [8, 9], current score: 17
You win!
```

---

## Game Rules

### Objective
Compete against the dealer to achieve a score closer to 21 without going over.

### Card Values
- **Number cards (2–10):** Worth their face value (e.g., 5 = 5 points).
- **Face cards (Jack, Queen, King):** Worth 10 points each.
- **Ace:** Can be worth 1 or 11, whichever benefits you more.

### Gameplay
1. **Your Turn:**
   - Start with 2 cards.
   - Choose:
     - **Hit:** Take another card.
     - **Stand:** Keep your current total.

2. **Dealer's Turn:**
   - The dealer starts with 2 cards.
   - The dealer must draw cards until their total is **17 or higher**.

3. **Winning Conditions:**
   - If your total is closer to 21 than the dealer's, you win.
   - If your total exceeds 21, you lose (**bust**).
   - If the dealer exceeds 21, you win.
   - If both totals are equal, it’s a tie.

---

## Enjoy Playing Blackjack!

