# Write your code here
def check(coords, top, bottom=1):
    for num in coords:
        if num.isalpha() or len(coords) != 2 or int(num) < bottom or int(num) > top:
            return False
    return True


print("Enter your board dimensions")
dim = input().split()
while not check(dim, 10):
    print("Invalid dimensions!\n")
    print("Enter your board dimensions")
    dim = input().split()

rows = int(dim[0])
columns = int(dim[1])
print("Enter the knight's starting position")
coord = input().split()
if not check(coord, columns):
    print("Invalid dimensions!")
else:
    x = int(coord[0])
    y = int(coord[1])
    cell_length = len(str(int(columns) * int(rows)))
    print(" {}".format("-" * (rows * (cell_length + 1) + 3)))
    for i in range(columns, 0, -1):
        print(str(i) + "|", end="")
        for j in range(1, rows + 1):
            if j == x and i == y:
                print(" " * cell_length + "X", end="")
            else:
                print(" {}".format("_" * cell_length), end="")
        print(" |")
    print(" {}".format("-" * (rows * (cell_length + 1) + 3)))
    print("  ", end="")
    for i in range(1, rows + 1):
        print(" " * cell_length + "{}".format(i), end="")
