from random import randint

scores = {"user":0,"computer":0}

class Board:
    """
    Creation of a standard board that will be used by the user and the computer. 
    The size, the number of ships, their position, and the owner of the board will be defined here.
    The ship positions and the guesses will be stocked here too.
    """
    def __init__ (self, size, num_ships, user_name, owner_type):
        """ Setup of the board blueprint """
        self.size = size
        self.board = [["."] * size for _ in range(size)] #Create a 2D board
        self.num_ships = num_ships
        self.user_name = user_name
        self.owner_type = owner_type
        self.ships_position = [] #List the effectiv position of the ship
        self.guesses = [] #List the guessed position of the ships

    def ships_place (self):
        """ Setup of the ships place """
        while len(self.ships_position) < self.num_ships:
            row= randint(0, self.size - 1)
            col= randint(0, self.size - 1)
            if (row, col) not in self.ships_position: #To avoid having twice the a ship at the same place
                self.ships_position.append ((row, col))
                if self.owner_type == "user":
                    self.board[row][col] = "S"

    def readme (self):
        """ Make the board a string so it's printable """
        return "\n".join([" ".join(row) for row in self.board])


def main():
    """
    Launch the game and run all functions
    """
    print ("*" * 50, "\n")
    print ( "Welcome to this great Battleship game !\n")
    name = input ("What's your name ?\n")
    print ("")
    print (f"So {name}, let's see if you got what it takes to beat your computer !\n")
    print ("*" * 50)

    user_board = Board(5,4,name,"user")
    computer_board = Board(5,4,"BigBlue", "computer")

    user_board.ships_place()
    computer_board.ships_place()

    print (f"{name} board")
    print (user_board.readme())
    print ("*" * 30, "\n")
    print ("Computer board")
    print (computer_board.readme())
    print ("*" * 30, "\n")

main ()















