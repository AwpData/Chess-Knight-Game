# Write your code here
def check(coords):
    for num in coords:
        if num.isalpha() or len(coords) > 2 or int(num) < 1 or int(num) > 8:
            return False
    return True


# just a test below
print("Enter the knight's starting position")
coord = input().split()
x = int(coord[0])
y = int(coord[1])
if not check(coord):
    print("Invalid dimensions!")
else:
    print(" -------------------")
    for i in range(8, 0, -1):
        print(str(i) + "|", end="")
        for j in range(1, 9):
            print(" X", end="") if j == x and i == y else print(" _", end="")
        print(" |")
    print(" -------------------")
    print("   1 2 3 4 5 6 7 8")
