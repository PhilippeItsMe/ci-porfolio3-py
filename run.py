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
        self.ships_position = [] #List the effectiv position of the ship, position will be removed everytime a ship is hit
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
        return "\n".join([" ".join(row) for row in self.board]) #To put all the stings together

    def user_guesses (self):
        """ Get the user guess and check his validity"""
        while True : 
            try : 
                print ("What's your guess ?")
                print (f"You need to enter a number between 0 and {self.size -1}.")
                row = int(input ("Your row :"))
                col = int(input ("Your col :"))
                if 0 <= row < self.size and 0 <= col < self.size:
                    if (row, col) not in self.guesses:
                        self.guesses.append((row, col))
                        return row, col
                    else:
                        print ("Oups, you already targeted this position.")
                else : print (f"Please enter a number between 0 and {self.size -1}.")
            except ValueError:
                print ("You input is invalid! Try again.")

    def computer_guesses (self):
        """ Make the computer guess"""
        row= randint(0, self.size - 1)
        col= randint(0, self.size - 1)
        if (row, col) not in self.guesses: #To avoid having twice the same comptuer guess
            return row, col

    def hit_or_missed (self, row, col):
        """Check if the targeted position is a hit or a missed"""
        if (col, row) in self.ships_position: 
            self.board[row][col] = "X"
            self.ships_position.remove (row, col)
            return "Hit"
        else:
            self.board[row][col] = "O"
            return "Miss"

    def game_not_over (self):
        """" To see if some ships are remaining """
        return len(self.ships_position) > 0
    
def main():
    """
    Launch the game and run all functions
    """
    # Welcome message
    print ("*" * 50, "\n")
    print ( "Welcome to my great Battleship game !\n")
    name = input ("What's your name ?\n")
    print ("")
    print (f"So {name}, let's see if you got what it takes to beat me !\n")
    print ("*" * 50)

    # Initial boards
    user_board = Board(5,4,name,"user")
    computer_board = Board(5,4,"BigBlue", "computer")
    user_board.ships_place()
    computer_board.ships_place()

    print (f"{name}, this is your board :")
    print (user_board.readme())
    print ("*" * 30, "\n")
    print ("And this is mine :")
    print (computer_board.readme())
    print ("*" * 30, "\n")

    #Game's on until all ships form one player are sunked
    while user_board.game_not_over() or computer_board.game_not_over():
        


main ()















