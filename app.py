# write 'hello world' to the console
import random


print('hello to the Game')

# Initialize game options and scores for both players
game_options = ['rock', 'paper', 'scissors']
player1_score = 0
computer_score = 0

# Function to get user input and handle invalid options
def get_user_input():
    user_input = input('Enter rock, paper, or scissors: ')
    if user_input not in game_options:
        print('Invalid option. Please try again.')
        return get_user_input()
    return user_input

# Function to get computer input and return a random option
def get_computer_input():
    
    comp_choice = random.choice(game_options)
    print(f'Computer chose: {comp_choice}')
    return comp_choice

# Function to determine the winner of the game
def determine_winner(player1, computer):
    if player1 == computer:
        return 'tie'
    elif player1 == 'rock' and computer == 'scissors':
        return 'player1'
    elif player1 == 'scissors' and computer == 'paper':
        return 'player1'
    elif player1 == 'paper' and computer == 'rock':
        return 'player1'
    else:
        return 'computer'   
    
# Function to print the winner of the game
def print_winner(winner):
    if winner == 'tie':
        print('It\'s a tie!')
    elif winner == 'player1':
        print('Player 1 wins!')
    else:
        print('Computer wins!')


# Function to print the current score
def print_score():
    print(f'Player 1: {player1_score} Computer: {computer_score}')

# Function to play the game
def play_game():
    global player1_score
    global computer_score
    player1 = get_user_input()
    computer = get_computer_input()
    winner = determine_winner(player1, computer)
    print_winner(winner)
    if winner == 'player1':
        player1_score += 1
    elif winner == 'computer':
        computer_score += 1
    print_score()


# Main game loop
def main():
    while True:
        play_game()
        play_again = input('Play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break

if __name__ == '__main__':
    main()


    