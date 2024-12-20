import art
import random

print(art.logo)

# Define the card values used in the game
cards = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
]  # Numbers + Face Cards (10) + Ace (11)

# Card values explanation:
# • Number cards: Their face value (e.g., 5 = 5 points).
# • Face cards: Jack, Queen, and King are worth 10 points each.
# • Ace: Can be worth 1 or 11, whichever benefits the player more. [Currently in the Deployment Phase]

# Initial card draw for player and dealer
player1_cards = random.sample(cards, 2)
computer_cards = random.sample(cards, 2)

print(f"player1_cards: {player1_cards}")

player1_cards_total = sum(player1_cards)  # sum of player1_cards
computer_cards_total = sum(computer_cards)

print(f"Your cards: {player1_cards}, current score: {player1_cards_total}")
print(f"Your cards: {computer_cards}, current score: {computer_cards_total}")

# Flag to determine when the game ends
game_over = False

def check_winner(player_score, dealer_score):
    """Check if either player has won the game."""
    if player_score > 21:
        print("You went over. You lose!")
        return True
    if dealer_score > 21:
        print("Dealer went over. You win!")
        return True
    if player_score == 21:
        print("BlackJack! You win!")
        return True
    if dealer_score == 21:
        print("BlackJack! You lose!")
        return True
    return False

# Initial check to determine if the game ends immediately
game_over = check_winner(player1_cards_total, computer_cards_total)

# Game loop
while not game_over:
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if user_choice == "y":
        player1_cards.append(random.choice(cards))
        player1_cards_total = sum(player1_cards)
        print(f"Your cards: {player1_cards}, current score: {player1_cards_total}")
        if player1_cards_total > 21:
            print("You went over. You lose!")
            game_over = True
    elif user_choice == "n":
        while computer_cards_total < 17:
            computer_cards.append(random.choice(cards))
            computer_cards_total = sum(computer_cards)
            print(
                f"Dealer's cards: {computer_cards}, current score: {computer_cards_total}"
            )
        if computer_cards_total > 21:
            print("Dealer went over. You win!")
        elif player1_cards_total > computer_cards_total:
            print("You win!")
        elif player1_cards_total < computer_cards_total:
            print("Dealer wins!")
        else:
            print("It's a tie!")
        game_over = True
    else:
        print("Invalid input. Please type 'y' or 'n'.")
