from random import randint

scores = {"user":0,"computer":0}

class Board:
    """
    Creation of a standard board that will be used by the user and the computer. 
    The size, the number of ships, their position, and the owner of the board will be defined here.
    The ship positions and the guesses will be stocked here too.
    """
    def __init__ (self, size, user_name, owner_type):
        self.size = size
        self.board =[["."] for x in range () for y in range(size)] #Create a 2D board
        self.num_ships = num_ships
        self.user_name = user_name
        self.owner_type = owner_type
        self.guesses = [] #List the guessed position of the ships
        self.ships_position = [] #List the effectiv position of the ship

    def ships_position (self):
        while len(self.ships_position) =< self.num_ships:
            row= randint(0, self.size - 1)
            col= randint(0, self.size - 1)
            if (row, col) not in self.ships_position: 
                self.ships_position.append ((row, col))



user_board = 














