# Write your code here
def check(coords, top, bottom=1):
    for num in coords:
        if num.isalpha() or len(coords) != 2 or int(num) < bottom or int(num) > top:
            return False
    return True


def get_coordinates():
    coord = input().split()
    if not check(coord, columns):
        print("Invalid dimensions!")
        return "Failed"
    return coord


def draw_board(coordinates, cols, row):
    x = int(coordinates[0])
    y = int(coordinates[1])
    cell_length = len(str(int(cols) * int(row)))
    print(" {}".format("-" * (row * (cell_length + 1) + 3)))
    for i in range(cols, 0, -1):
        print(str(i) + "|", end="")
        for j in range(1, row + 1):
            if j == x and i == y:
                print(" " * cell_length + "X", end="")
            else:
                print(" {}".format("_" * cell_length), end="")
        print(" |")
    print(" {}".format("-" * (row * (cell_length + 1) + 3)))
    print("  ", end="")
    for i in range(1, row + 1):
        print(" " * cell_length + "{}".format(i), end="")


print("Enter your board dimensions")
dim = input().split()
while not check(dim, 10):
    print("Invalid dimensions!\n")
    print("Enter your board dimensions")
    dim = input().split()

rows = int(dim[0])
columns = int(dim[1])

print("Enter the knight's starting position")
start = get_coordinates()
if start != "Failed":
    draw_board(start, columns, rows)
