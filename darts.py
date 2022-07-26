# Welcome section
print('Welcome to the Darts scoreboard!')
gameMode = input('Enter the number of players (1/2): ')
gameMode = int(gameMode)

def singlePlayer():
    print('You have 501 points at the beginning. There are 3 shots in each round. Please enter the points for each shot.')
    player1_score = 501
    shots = 0
    rounds = 1
    shotsInRound = 0

    while player1_score > 0:
        player1_shot = input('Please enter your points: ')
        player1_shot = int(player1_shot)
        player1_score = player1_score - player1_shot
        shots = shots + 1
        if player1_score < 0:
            player1_score = player1_score + player1_shot
            print('Too many points! Try again.')
            print('Current score: ', player1_score)
            continue
        shotsInRound = shotsInRound + 1

        if shotsInRound > 3:
            rounds = rounds + 1
            shotsInRound = 1

        print('Round ', rounds)
        print('Shots', shotsInRound, '/ 3')
        print('Current score: ', player1_score)

    if player1_score == 0:
        print('Congratulations! The game is over.', shots, 'shots')
        endGame = input('Do you want to play again? y/n: ')
        if endGame == 'y':
            singlePlayer()
        else:
            exit()

if gameMode == 1:
    print('Single Player game begin! Good luck!')
    singlePlayer()

######## -------------- #################################

def multiPlayer():
    print('Both players have 501 points at the beginning. There are 3 shots in each round per player. Please enter the points for each shot.')
    player1_score = 501
    player2_score = 501
    player1_shots = 0
    player2_shots = 0
    rounds = 1
    p1shotsInRound = 0
    p2shotsInRound = 0

    while player1_score and player2_score > 0:
        if p1shotsInRound < 3:
            player1_shot = input('Player 1: Please enter your points: ')
            player1_shot = int(player1_shot)
            player1_score = player1_score - player1_shot
            player1_shots = player1_shots + 1
            if player1_score < 0:
                player1_score = player1_score + player1_shot
                print('Too many points! Try again.')
                print('Player1 score: ', player1_score)
                continue
            p1shotsInRound = p1shotsInRound + 1
            p2shotsInRound = 0
            print('Player1 score: ', player1_score)
            print('Round ', rounds)
            print('Shots', p1shotsInRound, '/ 3')

        elif p2shotsInRound < 3:
            player2_shot = input('Player 2: Please enter your points: ')
            player2_shot = int(player1_shot)
            player2_score = player2_score - player2_shot
            player2_shots = player2_shots + 1

            if player2_score < 0:
                player2_score = player2_score + player2_shot
                print('Too many points! Try again.')
                print('Player2 score: ', player2_score)
                continue

            p2shotsInRound = p2shotsInRound + 1
            print('Player2 score: ', player2_score)
            print('Round ', rounds)
            print('Shots', p2shotsInRound, '/ 3')

            if p2shotsInRound > 3:
                p1shotsInRound = 0
                rounds = rounds + 1
                continue

    if player1_score == 0:
        print('Congratulations! The game is over.', 'player1 win!', player1_shots, 'shots')
        endGame = input('Do you want to play again? y/n: ')
        if endGame == 'y':
            multiPlayer()
        else:
            exit()
    elif player2_score == 0:
        print('Congratulations! The game is over.', 'player2 win!', player2_shots, 'shots')
        endGame = input('Do you want to play again? y/n: ')
        if endGame == 'y':
            multiPlayer()
        else:
            exit()
    

if gameMode == 1:
    print('Single Player game begin! Good luck!')
    singlePlayer()
elif gameMode == 2:
    print('Multi Player game begin. Good luck')
    multiPlayer()
