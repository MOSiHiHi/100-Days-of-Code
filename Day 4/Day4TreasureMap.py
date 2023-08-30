row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to place your the treasure?\n")
row = int(position[0])
column = int(position[1])
treasureRow = map[row - 1]
treasureRow[column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")