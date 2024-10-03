from random import randint

user_score = 0
computer_score = 0

class Board:
    """
    A class to represent the game board used by the user and the computer.
    
    Attributes:
        size (int): The size of the board (NxN).
        num_ships (int): Number of ships to be placed on the board.
        user_name (str): The name of the player (user or computer).
        owner_type (str): Indicates if the board belongs to the user or computer.
        ships_position (list): The list of coordinates where ships are placed.
        guesses (list): The list of coordinates guessed so far.
    """
    
    def __init__(self, size, num_ships, user_name, owner_type):
        """ Initializes the board. """
        self.size = size
        self.board = [["."] * size for _ in range(size)]
        self.num_ships = num_ships
        self.user_name = user_name
        self.owner_type = owner_type
        self.ships_position = []
        self.guesses = []

    def place_ships(self):
        """ Randomly places ships on the board. """
        while len(self.ships_position) < self.num_ships:
            row = randint(0, self.size - 1)
            col = randint(0, self.size - 1)
            if (row, col) not in self.ships_position:
                self.ships_position.append((row, col))
                if self.owner_type == "user":
                    self.board[row][col] = "S"

    def render_board(self):
        """ Returns the board as a printable string. """
        return "\n".join([" ".join(row) for row in self.board])

    def get_user_guess(self):
        """ Prompts the user for a valid row and column guess. """
        while True:
            try:
                row = int(input(f"Enter a row (0-{self.size - 1}): "))
                col = int(input(f"Enter a column (0-{self.size - 1}): "))
                if 0 <= row < self.size and 0 <= col < self.size:
                    if (row, col) not in self.guesses:
                        return row, col
                    else:
                        print("You already guessed that spot. Try again.")
                else:
                    print(f"Invalid input. Enter numbers between 0 and {self.size - 1}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_computer_guess(self):
        """ Generates a valid random guess for the computer. """
        while True:
            row = randint(0, self.size - 1)
            col = randint(0, self.size - 1)
            if (row, col) not in self.guesses:
                return row, col

    def check_hit_or_miss(self, row, col):
        """ Checks if the guess is a hit or miss. """
        if (row, col) in self.ships_position:
            self.board[row][col] = "X"
            self.ships_position.remove((row, col))
            print("Hit!")
            return "hit"
        else:
            self.board[row][col] = "O"
            print("Miss!")
            return "miss"

    def has_ships_left(self):
        """ Returns True if there are ships remaining on the board. """
        return len(self.ships_position) > 0


def setup_game():
    """ Sets up the game by initializing both user and computer boards. """
    print(f"\n")
    print("Welcome to my great Battleship! It's going to be bloody!")
    name = input("Please, enter your name: ").strip()
    while not name:
        name = input("Please enter a valid name: ").strip()
    
    user_board = Board(5, 4, name, "user")
    computer_board = Board(5, 4, "Computer", "computer")
    user_board.place_ships()
    computer_board.place_ships()
    
    return user_board, computer_board, name


def play_turn(board, opponent_board, is_user=True):
    """
    Handles a player's turn (user or computer).
    
    Args:
        board (Board): The current player's board.
        opponent_board (Board): The opponent's board.
        is_user (bool): Whether it's the user's turn or the computer's.
    """
    if is_user:
        print("\nYour turn, my friend!")
        row, col = board.get_user_guess()
    else:
        print("\n")
        print("My turn...(computer)")
        row, col = board.get_computer_guess()
        print(f"Computer guessed: Row {row}, Col {col}")

    board.guesses.append((row, col))
    return opponent_board.check_hit_or_miss(row, col)


def print_scores(user_score, computer_score, name):
    """ Prints the current scores. """
    print("\n")
    print(f"{name}'s score: {user_score}, Computer's score: {computer_score}")


def main():
    """ Main game loop. """
    global user_score, computer_score
    
    # Game setup
    user_board, computer_board, name = setup_game()
    
    print(f"\n{name}, this is your board:")
    print(user_board.render_board())
    print("\nThis is my board (computer - ships hidden):")
    print(computer_board.render_board())
    
    # Game loop
    while user_board.has_ships_left() and computer_board.has_ships_left():
        # User turn
        result = play_turn(user_board, computer_board, is_user=True)
        if result == "hit":
            user_score += 1
        print(f"\nMy board (computer) after your move:")
        print(computer_board.render_board())

        # Check if game over
        if not computer_board.has_ships_left():
            print("Congratulations! You won!")
            break

        # Computer turn
        result = play_turn(computer_board, user_board, is_user=False)
        if result == "hit":
            computer_score += 1
        print(f"\n{name}'s board after Computer's move:")
        print(user_board.render_board())

        # Check if game over
        if not user_board.has_ships_left():
            print("Sorry, you lost. The computer won!")
            break

        # Print current scores
        print_scores(user_score, computer_score, name)

if __name__ == "__main__":
    main()