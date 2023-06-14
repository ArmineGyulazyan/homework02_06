origin_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 16]]

for rows in range(len(origin_matrix)):
	for columns in range(len(origin_matrix[0])):
		print(origin_matrix[rows][columns], end=" ")
	print()
print()

for rows in range(len(origin_matrix) // 2):
	for columns in range(len(origin_matrix[0])):
		temp = origin_matrix[rows][columns]
		origin_matrix[rows][columns] = origin_matrix[len(origin_matrix) - 1 - rows][len(origin_matrix[0]) - 1 - columns]
		origin_matrix[len(origin_matrix) - 1 - rows][len(origin_matrix[0]) - 1 - columns] = temp

for rows in range(len(origin_matrix)):
	for columns in range(len(origin_matrix[0])):
		print(origin_matrix[rows][columns], end=" ")
	print()