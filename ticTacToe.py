import os

def clear():
	os.system('clear')

def display(board):
	print(f"""
	  {board[6]} | {board[7]} | {board[8]} 
	 -----------
	  {board[3]} | {board[4]} | {board[5]} 
	 -----------
	  {board[0]} | {board[1]} | {board[2]}\n""")

def markerSelect():
	player1 = player2 = None

	while player1 not in {'X', 'O', 'x', 'o'}:
	  player1 = input("Player 1, select 'X' or 'O': ")
	
	player1 = player1.upper()

	if player1 == 'X':
	  player2 = 'O'
	else:
	  player2 = 'X'
	
	print(f'Player 1: {player1}')
	print(f'Player 2: {player2}')
	
	return (player1, player2)

def getPosition(player, marks, board):
	while True:
	  playerInput = input(f'Player {player} ({marks[player-1]}), select position 1 - 9: ')

	  if not playerInput.isdigit():
	    continue
	  elif int(playerInput) not in range(1,10):
	    continue
	  elif board[int(playerInput)-1] != ' ':
	    print('Please, select empty field!')
	  else:
	    return int(playerInput)

def resultCheck(board, marks):
	indexes = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
	result = None
	tie = True

	for i in indexes:
	  vector = [board[i[j]-1] for j in range(0,3)]

	  if len(set(vector)) == 1 and vector[0] != ' ':
	    result = marks.index(vector[0]) + 1
	    clear()
	    display(board)
	    print(f'Player {result} has won! Congratulations!')
	    return result

	  if (len(set(vector)) == 1 and vector[0] == ' ') \
	    or (len(set(vector)) == 2 and ' ' in set(vector)):
	    tie = False

	if tie:
	  result = 0
	  clear()
	  display(board)
	  print("Game over! It's a tie!")

	return result

def continueGame():
	playerInput = None

	while playerInput not in {'Y', 'N', 'y', 'n'}:
	  playerInput = input('Do you want to play new game? [Y/N] ')
	
	if playerInput in {'Y', 'y'}:
	  return True
	else:
	  return False

play = True

print('Welcome in Tic Tac Toe game!')

while play:
  # Reset game board memory and control variables
  board = 9*[' ']
  result = None
  player = 1

  # Select players' marks
  marks = markerSelect()

  # Play until there is not a game result
  while result == None:

    # Display board
    display(board)

    # Get a player move
    position = getPosition(player, marks, board)

    # Update the board
    board[position-1] = marks[player-1]

    # Check game result
    result = resultCheck(board, marks)

    # Ask for another game
    if result != None:
      play = continueGame()

    # Switch players
    if player == 1:
      player = 2
    else:
      player = 1

    # Clear screen
    clear()

