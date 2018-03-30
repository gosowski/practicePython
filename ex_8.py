scorePlayerOne = int(0)
scorePlayerTwo = int(0)

while True:
    print("To end game, enter 'q'")
    playerOne = input("Player one: ")
    playerTwo = input("Player two: ")

    if playerOne == 'rock':
        if playerTwo == 'scissors':
            scorePlayerOne+=1
        else:
            scorePlayerTwo+=1
    elif playerOne == 'paper':
        if playerTwo == 'rock':
            scorePlayerOne+=1
        else:
            scorePlayerTwo+=1
    elif playerOne == 'scissors':
        if playerTwo == 'paper':
            scorePlayerOne+=1
        else:
            scorePlayerTwo+=1

    if playerOne == 'q' or playerTwo == 'q':
        break;
    else:
        print("Invalid input!")

if scorePlayerOne > scorePlayerTwo:
    print("Player one won {} to {}".format(scorePlayerOne, scorePlayerTwo))
elif scorePlayerOne == scorePlayerTwo:
    print("Draw")
else:
    print("Player two won {} to {}".format(scorePlayerTwo, scorePlayerOne))
