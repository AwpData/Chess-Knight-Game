# Write your code here

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def draw_board(self, coordinates, x, y):  # coordinates will be a list
        cell_length = len(str(int(self.columns) * int(self.rows)))
        print(" {}".format("-" * (self.rows * (cell_length + 1) + 3)))
        for i in range(self.columns, 0, -1):
            print(str(i) + "|", end="")
            for j in range(1, self.rows + 1):
                if j == x and i == y:
                    print(" " * cell_length + "X", end="")
                    continue
                for k in range(0, len(coordinates)):
                    if j == int(coordinates[k][0]) and i == int(coordinates[k][1]):
                        print(" " * cell_length + "O", end="")
                        break
                else:
                    print(" {}".format("_" * cell_length), end="")
            print(" |")
        print(" {}".format("-" * (self.rows * (cell_length + 1) + 3)))
        print("  ", end="")
        for i in range(1, self.rows + 1):
            print(" " * cell_length + "{}".format(i), end="")

    def check_coordinates(self, position):
        for pos in position:
            if pos.isalpha() or len(position) != 2 or int(pos) < 1 or int(pos) > self.columns:
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

    def get_valid_pos(self, x, y):
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
        self.draw_board(valid_moves, x, y)


board = Board(0, 0)
print("Enter your board dimensions")
dim = input().split()
while True:
    for num in dim:
        if num.isalpha() or len(dim) != 2 or int(num) < 0:
            print("Invalid dimensions!\n")
            print("Enter your board dimensions")
            dim = input().split()
            break
    else:
        break

board.set_rows(int(dim[0]))
board.set_cols(int(dim[1]))

print("Enter the knight's starting position")
coords = input().split()
if not board.check_coordinates(coords):
    print("Invalid dimensions!")
else:
    board.get_valid_pos(int(coords[0]), int(coords[1]))
