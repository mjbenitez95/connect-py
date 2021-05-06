import random

NUM_ROWS = 6
NUM_COLS = 7
PLAYER_NUM = 1
CPU_NUM = 2

class Board:
    def __init__(self):
        self.board = []
        for _ in range(NUM_ROWS):
            single_row = [0] * NUM_COLS
            self.board.append(single_row)

    def __str__(self):
        board_display = ""
        for row in self.board:
            board_display += str(row)
            board_display += "\n"
        return board_display

    def display(self):
        for row in self.board:
            print row
        print "-" * NUM_COLS * 3

    def drop(self, column, player):
        if self.board[0][column] != 0:
            return False
        for row in range(1, NUM_ROWS):
            if self.board[row][column] != 0:
                self.board[row-1][column] = player
                return True
            elif (row == NUM_ROWS - 1):
                self.board[row][column] = player
                return True

def prompt_player_move():
    print "Where would you like to drop a coin?"
    player_input = input()
    return int(player_input)

if __name__ == "__main__":
    board = Board()
    turn_number = 1
    while True:
        if turn_number % 2 == PLAYER_NUM:
            move = prompt_player_move()
            while board.drop(move, PLAYER_NUM) is False:
                print "Invalid move. Please try again."
                move = prompt_player_move()
        else:
            # make computer move
            random_move = random.choice(range(NUM_COLS))
            while board.drop(random_move, CPU_NUM) is False:
                random_move = random.choice(range(NUM_COLS))
        board.display()
        turn_number += 1
        
            

