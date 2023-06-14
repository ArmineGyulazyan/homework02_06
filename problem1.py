zeroM_list = [[0, 'M', 0, 'M', 0], [0, 0, 'M', 0, 0], [0, 0, 0, 0, 0], ['M', 'M', 0, 0, 0], [0, 0, 0, 'M', 0]]

for row in range(len(zeroM_list)):
    for column in range(len(zeroM_list[0])):
        print(zeroM_list[row][column], end=" ")
    print()

for row in range(len(zeroM_list)):
    for column in range(len(zeroM_list[0])):
        count_m = 0
        if zeroM_list[row][column] == 0:
            if row != 0 or column != 0:
                start_row = row - 1 if row - 1 >= 0 else row
                end_row = row + 2 if row + 2 <= len(zeroM_list) else len(zeroM_list)
                start_column = column - 1 if column - 1 >= 0 else column
                end_column = column + 2 if column + 2 <= len(zeroM_list[0]) else len(zeroM_list[0])
                for i in range(start_row, end_row):
                    for j in range(start_column, end_column):
                        if zeroM_list[i][j] == 'M':
                            count_m += 1
                zeroM_list[row][column] = count_m
            else:
                for i in range(row, row + 2):
                    for j in range(column, column + 2):
                        if i < len(zeroM_list) and j < len(zeroM_list[0]) and zeroM_list[i][j] == 'M':
                            count_m += 1
                zeroM_list[row][column] = count_m

print()
for row in range(len(zeroM_list)):
    for column in range(len(zeroM_list[0])):
        print(zeroM_list[row][column], end=" ")
    print()
