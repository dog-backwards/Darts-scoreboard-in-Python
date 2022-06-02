# Welcome section
print('Welcome to the Darts scoreboard. You have 501 points at the beginning. There are 3 shots in each round. Please enter the points for each shot.')
player1_score = 501
shots = 0

while player1_score > 0:
    player1_shot = input('Please enter your points:')
    player1_shot = int(player1_shot)
    player1_score = player1_score - player1_shot
    shots = shots + 1
    if player1_score < 0:
        player1_score = player1_score + player1_shot
        print('Too many points! Try again')
        print('Current score: ', player1_score)
        continue
    print('Current score: ', player1_score)

if player1_score == 0:
    print('Congratulations! The game is over.', shots, 'shots')
