#  laocal search :
    # doesnt keep track of all possible paths, just small sets of potientail solutions
    # have an objective function which can be continous 
# State-Space Landscape
    # Location (AKA state)
    # Elevation (AKA objective function)
    # if elevation is cost, find global minimum (valley)

# Hill Climbing 
    # look at all successors of the state and it will look at the highets value successor and call it the neighbor  
        # if the value is greater the the current value then update (current = neighbor)
# key take away (TAKES THE HIGHEST VALUE)

    # Heuristic h = number of queen attacking each other directly or indirectly (cost function) -> try and find the minumum
    # Succesors are all possible states moving one Q in the same column 
    # 8 (Queens) x 7 (positions for each column) = 56 possible successors


# Board 
import random


board = [0, 0, 0, 0, 0, 0, 0, 0]
starting_board = board

def board_representation(board_p):
    new_baord = []
    for i in range(len(board)):
        new_baord.append(i, board_p[i])
    print(new_baord)

    for i in range(len(board)):
        for j in range(len(board)):
            if [j, i] in new_baord:
                print("Q", end=" ")
            else:
                print(".", end=" ")

# this fucntion determines the heuristic cost of the new board
# heuristic cost = number of queens attacking one anotehr 
def find_h_cost(board):
    h = 0

    # check all of the queens
    for i in range(len(board)):
        # check and see what interations are happening with the queens
        for j in range(i + 1, len(board)):
            # if the queen is in the same colum get the offset 
            if board[i] == board[j]:
                h += 1

            # offset 
            offset = i - j

            # see if there is a diagonal interaction with the queens
            if board[i] == board[j] + offset or board[i] == board[j] - offset:
                h += 1
    return h


# this function determines what the next best move is based on the h cost that we calculated out in the previous function 
# there are 56 neighboring states (8 x 7) there are 8 queens and 7 positons each queen can move to 
def next_best_move(board):
    #store the moves in an array 
    moves = []
    # add the moves taken to the array along with the h cost of move 
    moves.append([board, find_h_cost(board)])

    for col in range(len(board)):
        for row in range(len(board)):
            copy_of_board = list(board)
            if board[col] == row:
                continue
            copy_of_board[col] = row
            cost_of_move = find_h_cost(copy_of_board)
            moves.append([copy_of_board, cost_of_move])
    current = find_h_cost(board)

    for row in moves:
        if row[1] > current:
            current = row[1]

    # there can be more than 1 bets move to go to because the h cost might be the same 
    best_move_for_cost = []
    for row in moves:
        if row[1] == current:
            best_move_for_cost.append(row[0])
    
    # randomly select one move out of all of the best moves 
    random_next_move = random.choice(best_move_for_cost)

    return random_next_move

# show the initial state of the board and the h cost 
board_representation(board)
print("h = " + str(find_h_cost(board)))
print()


action_sequence = []


