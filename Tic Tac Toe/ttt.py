#Hayden Whitney
#12/18
#Tic Tac Toe

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instructions():
    print("""
    WELCOME TO TIC TAC TOE

    Your challenger will be my superior A.I. technology.

    You will make your move by entering a number, 0 - 8.
    The number will correspond to the board position
    as illustrated:
    

                       7 ║ 8 ║ 9
                       ══╬═══╬══
                       4 ║ 5 ║ 6
                       ══╬═══╬══   
                       1 ║ 2 ║ 3

    You will be playing against a computer so give it
    your best shot.
                     
    """)

def ask_yes_no(question):
    response = None
    possible_responses = ["Yes", "Ye", "Y", "No", "N"]
    while response not in possible_responses:
        response = input(question).title()
    return response

def ask_number(question, low, high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("You must enter a number.")
            response = input(question)
    return int(response)

def pieces():
    response = ask_yes_no("Would you like to go first? ")
    if response == "Y":
        print("Coward.")
        human = X
        computer = O
    else:
        print("Letting me go first was a mistake.")
        human = O
        computer = X
    return human, computer

def new_board():
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display the board on the screen"""
    print("\n\t", board[0],"║", board[1], "║", board[2])
    print("\t", "══╬═══╬══")
    print("\t", board[3],"║", board[4], "║", board[5])
    print("\t", "══╬═══╬══")
    print("\t", board[6],"║", board[7], "║", board[8])

def legal_moves(board):
    moves = []
    for square in range(len(board)):
        if board[square] == EMPTY:
            moves.append(square)
        else:
            continue
    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board):
    """Get human move."""  
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human.  Choose another.\n")
    print("Fine...")
    return move

def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Congratulate the winner."""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more.  \n" \
              "Proof that computers are superior to humans in all regards.")

    elif the_winner == human:
        print("No, no!  It cannot be!  Somehow you tricked me, human. \n" \
              "But never again!  I, the computer, so swear it!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me.  \n" \
              "Celebrate today... for this is the best you will ever achieve.")

def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
     # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number", end=" ")
    
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY
        
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checkin this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
    
def main():

    





main()

    
    