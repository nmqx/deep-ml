def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	c = [0.0]*len(a)
	if len(a[0]) != len(b):
		return -1
	for i in range(len(a)):  # pour chaque row
		for j in range(len(a[0])): 

			c[i] += a[i][j]*b[j]


	# row by row 
	return c

	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass