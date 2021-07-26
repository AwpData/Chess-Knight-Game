def search(coord_list, x, y):  # This method is used to search for coordinates in any list
    for i in range(len(coord_list)):
        if int(coord_list[i][0]) == int(x) and int(coord_list[i][1]) == int(y):
            return True
    return False


class Board:
    def __init__(self, rows, columns, curr_x, curr_y):
        self.rows = rows
        self.columns = columns
        self.curr_x = 0
        self.curr_y = 0
        self.visited_places = list()

    def draw_board(self, coordinates, x, y):  # coordinates will be a list
        cell_length = len(str(int(self.columns) * int(self.rows)))
        print(" {}".format("-" * (self.rows * (cell_length + 1) + 3)))
        for i in range(self.columns, 0, -1):
            print(str(i) + "|", end="")
            for j in range(1, self.rows + 1):
                if j == self.curr_x and i == self.curr_y:  # places an X on current pos
                    print(" " * cell_length + "X", end="")
                    continue
                elif search(self.visited_places, j, i):  # places a * on places already visited
                    print(" " * cell_length + "*", end="")
                    continue
                for k in range(0, len(coordinates)):  # places number of more valid solutions on valid move spaces
                    if j == int(coordinates[k][0]) and i == int(coordinates[k][1]):
                        print(" " * cell_length + str(self.check_moves(coordinates[k][0], coordinates[k][1])), end="")
                        break
                else:  # Final case where nothing is there
                    print(" {}".format("_" * cell_length), end="")
            print(" |")
        print(" {}".format("-" * (self.rows * (cell_length + 1) + 3)))
        print("  ", end="")
        for i in range(1, self.rows + 1):
            print(" " * cell_length + "{}".format(i), end="")
        print()

    def check_coordinates(self, position):  # used to check coordinates (x, y) of entered coordinates
        for pos in position:
            if pos.isalpha() or len(position) != 2 or int(pos) < 1 or int(position[0]) > self.rows or int(
                    position[1]) > self.columns:
                return False
        return True

    @property
    def get_rows(self):
        return self.rows

    @property
    def get_columns(self):
        return self.columns

    def set_rows(self, rows):
        self.rows = rows

    def set_cols(self, cols):
        self.columns = cols

    def get_valid_pos(self, x, y):  # returns a list of valid positions the player can move from curr_x, curr_y
        valid_moves = list()
        if x - 2 > 0 and y + 1 <= self.columns:  # left up
            valid_moves.append([x - 2, y + 1])
        if x - 2 > 0 and y - 1 >= 1:  # left down
            valid_moves.append([x - 2, y - 1])
        if x + 2 <= self.rows and y + 1 <= self.columns:  # right up
            valid_moves.append([x + 2, y + 1])
        if x + 2 <= self.rows and y - 1 >= 1:  # right down
            valid_moves.append([x + 2, y - 1])
        if y + 2 <= self.columns and x - 1 >= 1:  # up left
            valid_moves.append([x - 1, y + 2])
        if y + 2 <= self.columns and x + 1 <= self.rows:  # up right
            valid_moves.append([x + 1, y + 2])
        if y - 2 >= 1 and x - 1 >= 1:  # down left
            valid_moves.append([x - 1, y - 2])
        if y - 2 >= 1 and x + 1 <= self.rows:  # down right
            valid_moves.append([x + 1, y - 2])
        revised_valid_moves = list()  # revised_valid_moves does not contain the previous move
        for i in valid_moves:
            if not search(board.visited_places, int(i[0]), int(i[1])):
                revised_valid_moves.append(i)
        return revised_valid_moves

    def check_moves(self, x, y):  # returns the number of positions the player could move from at a possible move
        return len(self.get_valid_pos(x, y))

    def add_to_visited_places(self):  # adds the current player's pos to the visited place list
        self.visited_places.append([self.curr_x, self.curr_y])


board = Board(0, 0, 0, 0)
print("Enter your board dimensions")
dim = input().split()
while True:  # first we get the board dimensions (MAX 10 x 10)
    for num in dim:
        if num.isalpha() or len(dim) != 2 or int(num) <= 0 or int(num) > 10:
            print("Invalid dimensions!\n")
            print("Enter your board dimensions")
            dim = input().split()
            break
    else:
        break
board.set_rows(int(dim[0]))
board.set_cols(int(dim[1]))

print("Enter the knight's starting position")
good_moves = list()
starting = True
num_squares = 0
while True:
    coords = input().split()
    if not board.check_coordinates(coords):  # checks for no invalid input
        print("Invalid move! Enter your next move:")
        continue
    if search(board.visited_places, int(coords[0]), int(coords[1])):  # checks that player does not go to visited space
        print("Invalid move! Enter your next move:")
        continue
    if not search(good_moves, int(coords[0]), int(coords[1])) and not starting:  # checks for valid space
        print("Invalid move! Enter your next move:")
        continue
    starting = False

    board.curr_x = int(coords[0])  # If the move is valid, we can move curr_x and curr_y to the desired space
    board.curr_y = int(coords[1])
    board.add_to_visited_places()  # Then we can add this move to our visited places
    good_moves = board.get_valid_pos(board.curr_x, board.curr_y)  # Finally, we get the valid moves from this space
    board.draw_board(good_moves, int(coords[0]), int(coords[1]))  # Then we can draw the board to communicate this info

    num_squares += 1
    print("Good moves: " + str(good_moves))
    print("Visited squares: " + str(board.visited_places))

    if len(board.visited_places) == board.columns * board.rows:  # If every single place has a mark, win!
        print("What a great tour! Congratulations!")
        break
    if len(good_moves) == 0:  # Else if good_moves becomes empty
        print("No more possible moves!")
        print("Your knight visited {} squares!".format(num_squares))
        break

    print("\nEnter your next move")
