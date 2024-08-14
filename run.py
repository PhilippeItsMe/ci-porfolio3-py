from random import randint

user_score = 0
computer_score = 0

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
                print ("What's your guess ?\n")
                print (f"You need to enter a number between 0 and {self.size -1}.\n") 
                row = int(input ("Your row : ")) 
                col = int(input ("Your col : ")) 
                if 0 <= row < self.size and 0 <= col < self.size:
                    if (row, col) not in self.guesses:
                        return row, col
                    else:
                        print("\n")
                        print ("Oups, you already targeted this position. Try again.")
                        print("\n")
                else : 
                    print("\n")
                    print (f"You need to enter a number between 0 and {self.size -1}, try again.") 
                    print("\n")
            except ValueError:
                print("\n")
                print ("You input is invalid! Try again.")
                print("\n")

    def computer_guesses (self):
        """ Make the computer guess"""
        while True: 
            row= randint(0, self.size - 1)
            col= randint(0, self.size - 1)
            if (row, col) not in self.guesses: #To avoid having twice the same comptuer guess
                return row, col

    def hit_or_missed (self, row, col):
        """Check if the targeted position is a hit or a missed"""
        if (row, col) in self.ships_position: 
            self.board[row][col] = "X"
            self.ships_position.remove ((row, col))
            print ("That's a hit.")
            return "hit"
        else:
            self.board[row][col] = "O"
            print ("That's a miss.")

    def game_not_over (self):
        """" To see if some ships are remaining """
        return len(self.ships_position) > 0
    
def main():
    """
    Launch the game and run all functions
    """
    # Welcome message
    print ("\n")
    print ("*" * 30, "\n")
    print ( "Welcome to my great Battleship game !\n")
    name = input ("What's your name ?\n")
    print ("")
    print (f"So {name}, let's see if you got what it takes to beat me !\n")
    print ("*" * 30)

    # Initiat the boards
    user_board = Board(3,2,name,"user")
    computer_board = Board(3,2,"BigBlue", "computer")
    user_board.ships_place()
    computer_board.ships_place()

    print (f"\n{name}, this is your board : ")
    print (user_board.readme())
    print ("\n")
    print ("And this is mine : (of course my ships are hidden)")
    print (computer_board.readme())
    print ("\n")
    print ("*" * 30, "\n")

    #Game's on until all ships form one player are sunked
    while user_board.game_not_over() and computer_board.game_not_over():
        
        #User playing
        row, col = user_board.user_guesses () #Take the result of the methode
        user_board.guesses.append ((row, col))
        result = computer_board.hit_or_missed (row, col) #Check if the user hit or missed
        print("\n")
        print ("My new board is :")
        print (computer_board.readme())
        print("\n")
        print ("*" * 30, "\n")

        #Check if the user won
        if not computer_board.game_not_over():
            print ("Well done, you won ! The game is over.")
            print("\n")
            break

        #Computer playing
        row, col = user_board.computer_guesses () #Take the result of the method
        computer_board.guesses.append ((row, col))
        print (f"My guess is row : {row} and col : {col}")
        result = user_board.hit_or_missed (row, col) #Check if the user hit or missed
        print("\n")
        print (f"{name}, your new board is :")
        print (user_board.readme())
        print("\n")
        print ("*" * 30, "\n")

        #New score printing
        if user_board.hit_or_missed() == "hit":
            computer_score += 1
        if computer_board.hit_or_missed() == "hit":
            user_score += 1
        print (f"{name}, your new score is {user_score} and mine is {computer_score}")
        print("\n")
        print ("*" * 30, "\n")
        
        #Check if the computer won
        if not user_board.game_not_over():
            print ("Hey hey hey... I got you ! I won. The game is over.")
            print("\n")
            break

        #Check if the user still want to play
        a = input ("Are you ready for the next round ? If yes, press 'y' : ")
        print("\n")
        if a == "y":
            continue
        else :
            break

main ()