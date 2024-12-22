import random

# Define the card values used in the game
cards = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
    11,  # ACE
]

player1_cards = random.sample(cards, 2)
computer_cards = random.sample(cards, 2)

player1_cards_total = sum(player1_cards)  # sum of player1_cards
computer_cards_total = sum(computer_cards)

print(f"Your cards: {player1_cards}, current score: {player1_cards_total}")
print(f"Computer cards: {computer_cards}, current score: {computer_cards_total}")

# Flag to determine when the game ends
game_over = False


# Function to check for a winner or if the game is over
def check_winner(player_score, dealer_score):
    """Check if either player has won the game."""
    # ACE is 1 or 11 points
    if player_score + 11 <= 21:
        player_score += 11
    elif player_score + 1 <= 21:
        player_score += 1
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

while not game_over:
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    match user_choice:
        case "y":
            player1_cards.append(random.choice(cards))
            player1_cards_total = sum(player1_cards)
            print(
                f"Your cards: {player1_cards}, current score: {player1_cards_total} & Computer score: {computer_cards_total}"
            )
            if player1_cards_total > 21:
                print("Busted. You lose!")
                game_over = True
        case "n":
            while computer_cards_total < 17:
                computer_cards.append(random.choice(cards))
                computer_cards_total = sum(computer_cards)
                print(
                    f"Dealer's cards: {computer_cards}, current score: {computer_cards_total} & Player score: {player1_cards_total}"
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
        case _:
            print("Invalid input. Please type 'y' or 'n'.")
