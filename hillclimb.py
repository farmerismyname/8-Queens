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

board = [0,7,3,5,4,1,3,6]
starting_board = board

#loop
cases = int(input("how many cases?\n"))
def board_representation(board_p):
    new_board = []
    #visualize the board
    for i in range(len(board)):
        new_board.append(i, board_p[i])
    print(new_board)

    for i in range(len(board)):
        for j in range(len(board)):
            if [j, i] in new_board:
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
    # store the moves in an array
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
#board_representation(board)
print("h = " + str(find_h_cost(board)))
print()

action_sequence = []


def queens_in_conflict(board):
    q_conflict = []


    for col in range(0,7):
        row = board[col]
        og_col = col
        for comp_col in range(0, 7):
            if (comp_col != og_col):
                # check for row conflicts
                if (row == board[comp_col]):
                    #avoid dups
                    if og_col not in q_conflict:
                        q_conflict.append(og_col)
                #if absolute value of row diff = col diff ->conflict
                if (abs(comp_col - og_col) == abs(row - board[comp_col])):
                    if og_col not in q_conflict:
                        q_conflict.append(og_col)
            #return array of the columns with a queen that has a conflict
    return(q_conflict)

def pick_queen(board):
    options = queens_in_conflict(board)
    num = random.randint(0,len(options)-1)
    return options[num]

#calculate conflicts for selected queen
def calc_conflicts(board,column):
    conflicts = 0

    for columns in range(7):
        if columns != column:
            #check for diagnol conflict
            if ((abs(column - columns) == abs(board[column] - board[columns]))):
                conflicts = conflicts + 1
            #check for row conflict
            if (board[column] == board[columns]):
                conflicts = conflicts + 1

    return conflicts



#pick next move for a queen with conflicts
def min_conflicts_decision(board,column):
    #initial variables
    og_board = board
    options = []
    min_conflicts = calc_conflicts(board, column)
    #place queen in every row and calc conflicts
    for row in range (0,7):
        board[column] = row
        #create board
        current_board = []
        for i in range(0,7):
            if i != column:
                current_board.append(og_board[i])
        else:
            current_board.append(row)

        #calc conflicts for current board
        current_conflicts = calc_conflicts(current_board, column)
        if (current_conflicts <= min_conflicts):
            min_conflicts = current_conflicts
            options.append(current_board)
            if current_conflicts < min_conflicts:
                options = [current_board]


    rand = random.randint(0,len(options)-1)
    return options[rand]


print(queens_in_conflict(starting_board))
board_representation(starting_board)
