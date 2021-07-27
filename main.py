import time


def search(coord_list, x, y):  # This method is used to search for coordinates in any list
    for i in range(len(coord_list)):
        if int(coord_list[i][0]) == int(x) and int(coord_list[i][1]) == int(y):
            return True
    return False


solved_board = list()  # For the auto-solver
x_moves = [2, 1, -1, -2, -2, -1, 1, 2]  # x_moves and y_moves are possible moves if put together Ex. [2 right, 1 down]
y_moves = [1, 2, 2, 1, -1, -2, -2, -1]


class Board:
    def __init__(self, rows, columns):
        self.rows = int(rows)
        self.columns = int(columns)
        self.curr_x = 0
        self.curr_y = 0
        self.visited_places = list()

    def draw_board(self, coordinates, solved=False):  # coordinates will be a list
        cell_length = len(str(int(self.columns) * int(self.rows)))
        print(" {}".format("-" * (self.rows * (cell_length + 1) + 3)))
        for i in range(self.columns, 0, -1):
            print(str(i) + "|", end="")
            for j in range(1, self.rows + 1):
                if solved:
                    for k in range(0, len(solved_board)):
                        if j == int(solved_board[k][0]) and i == int(solved_board[k][1]):
                            print(" " * cell_length + str(solved_board[k][2]), end="")
                            continue
                elif j == self.curr_x and i == self.curr_y:  # places an X on current pos
                    print(" " * cell_length + "X", end="")
                    continue
                elif search(self.visited_places, j, i):  # places a * on places already visited
                    print(" " * cell_length + "*", end="")
                    continue
                if not solved:
                    for k in range(0, len(coordinates)):  # places number of more valid solutions on valid move spaces
                        if j == int(coordinates[k][0]) and i == int(coordinates[k][1]):
                            print(" " * cell_length + str(self.check_moves(coordinates[k][0], coordinates[k][1])),
                                  end="")
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
            if (pos.isalpha() or len(position) != 2 or int(pos) < 1 or int(position[0]) > self.rows or int(
                    position[1]) > self.columns):
                return False
        return True

    @property
    def get_rows(self):
        return self.rows

    @property
    def get_columns(self):
        return self.columns

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

    def find_solution(self, row, col, counter):  # finds the proper solution using recursion
        counter = counter
        for i in range(8):
            if counter > self.rows * self.columns:  # This checks if every single space is covered in a step
                return True
            new_x = row + x_moves[i]  # Both of these update the x and y
            new_y = col + y_moves[i]
            if self.check_coordinates([str(new_x), str(new_y)]) and not search(self.visited_places, int(new_x),
                                                                               int(new_y)):
                solved_board.append([new_x, new_y, counter])  # If it is valid, then we can append it to solved board
                board.curr_x = new_x  # Update new current Pos for x and y
                board.curr_y = new_y
                self.add_to_visited_places()  # Add it to the visited places so we don't hit it again
                if self.find_solution(new_x, new_y, counter + 1):  # Use recursion to check the new spot now
                    return True
                solved_board.pop()  # Else, remove that new coordinate because it is a dead end
                board.visited_places.pop()  # Also, remove it from visited spaces since we have to visit again
        return False  # There is no solution

    def check_moves(self, x, y):  # returns the number of positions the player could move from at a possible move
        return len(self.get_valid_pos(x, y))

    def add_to_visited_places(self):  # adds the current player's pos to the visited place list
        self.visited_places.append([self.curr_x, self.curr_y])


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

board = Board(dim[0], dim[1])

while True:  # Next, get a valid starting position within our board
    print("Enter the knight's starting position")
    coords = input().split()
    if not board.check_coordinates(coords):  # checks for no invalid input
        print("Invalid starting position!")
        continue
    else:
        break

good_moves = list()
num_squares = 0
solver = input("Do you want to see a solution to the puzzle? (y/n) ")
if solver == "y":  # Show the solution!
    solved_board.append([int(coords[0]), int(coords[1]), 1])
    board.curr_x = int(coords[0])
    board.curr_y = int(coords[1])
    board.add_to_visited_places()
    start = time.perf_counter()
    if board.find_solution(int(coords[0]), int(coords[1]), 2):  # Found a solution
        stop = time.perf_counter()
        print(f"\nFound solution in {stop - start:0.2f} seconds!")
        board.draw_board(solved_board, True)
    else:  # Did not find a solution
        print("No solution exists!")

elif solver == "n":  # User wants to solve it themselves
    while True:
        if int(dim[0]) < 4 and int(dim[1]) < 4:  # Firstly, any dimensions below 4 are unsolvable (no 0 or 1 cases)
            print("No solution exists!")
            break

        board.curr_x = int(coords[0])  # If the move is valid, we can move curr_x and curr_y to the desired space
        board.curr_y = int(coords[1])
        board.add_to_visited_places()  # Then we can add this move to our visited places
        good_moves = board.get_valid_pos(board.curr_x, board.curr_y)  # Get valid moves for this space
        board.draw_board(good_moves)  # Draw board to communicate above info

        print("Good moves: " + str(good_moves))
        print("Visited squares: " + str(board.visited_places))

        if len(board.visited_places) == board.columns * board.rows:  # If every single place has a mark, win!
            print("What a great tour! Congratulations!")
            break
        if len(good_moves) == 0:  # Else if good_moves becomes empty
            print("No more possible moves!")
            print("Your knight visited {} squares!".format(num_squares))
            break

        while True:  # Now we need to get the input again for the next move
            print("\nEnter your next move")
            coords = input().split()
            if not board.check_coordinates(coords):  # checks for no invalid input
                print("Invalid move!", end="")
            elif search(board.visited_places, int(coords[0]), int(coords[1])):  # prevents visiting visited spaces
                print("Invalid move!", end="")
            elif not search(good_moves, int(coords[0]), int(coords[1])):  # checks for valid space
                print("Invalid move!", end="")
            else:
                num_squares += 1
                break
