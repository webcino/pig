import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input('Enter the number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if players >= 2 and players <= 4:
            break
        else:
            print('Please enter a number between 2 and 4.')
    else:
        print('Invalid input, try again.')

max_score = 50
player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores) < max_score:
    for player_index in range(players):
        print('Player', player_index + 1, 'turn just started!\n')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y)?')
            if should_roll.lower() == 'y':
                break

            value = roll()
            if value == 1: 
                print('You rolled a 1! Turn Done!')
                current_score = 0
            else:
                current_score += value
                print('You rolled a: ', value)

            print('Your score is:', current_score)
        
        player_scores[player_index] += current_score
        print('Your total score is:', player_scores[player_index])
