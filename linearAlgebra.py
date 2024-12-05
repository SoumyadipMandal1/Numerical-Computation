import copy

def gaussianElimination(a, b):
	'''
	Input:
	a: Coefficient Matrix
	b: Augmented Array

	This function takes a coefficient matrix and augmented vector as input.
	It retpresents a system of n equations in n variables
	This function returns an array of solution of the system
	'''

	# Copying the matrix and array so that the original data type does not change
	coefficient = copy.copy(a) # Coefficient Matrix
	augmented = b.copy() # Augmented array

	####### CHECKING THE DIMENSIONS OF THE INPUT ################

	if (rows := len(coefficient)) == 0:
		raise ValueError("Empty Matrix")

	columns = len(coefficient[0])

	# Checking if all rows have the same length
	for i in coefficient[1:]: # Starting with second row because we are comparing it with the length of second row
		if len(i) != columns:
			raise TypeError("All rows of a matrix is of the same length")

	# Checking whether the matrix is square matrix or not
	if rows != columns:
		raise TypeError("The matrix is not a square matrix")

	# Checking whether the array is of the same size or not
	if columns != len(augmented):
		raise TypeError("The size of each dimension of matrix should be equal to the length of the array")

	############## SOLVING THE EQUATION ######################

	# Let us consider the rows as size
	size = rows
	del columns

	# Converts the matrix into row echelon form

	for i in range(size):

		# If pivot is zero
		if coefficient[i][i] == 0:

			# Searching for a non-zero number below the pivot
			for j in range(i + 1, size):
				if coefficient[j][i]:

					# Swapping two rows
					coefficient[i], coefficient[j] = coefficient[j], coefficient[i]
					augmented[i], augmented[j] = augmented[j], augmented[i]
					break

			# If all the numbers in the column is zero
			else:
				raise ValueError("Matrix is singular")
			
		# Changing all the numbers below the pivot in the same column zero
		for j in range(i + 1, size):
			# If scalingFactor is zero, then there will be no changes
			if coefficient[j][j] == 0:
				continue
			scalingFactor = coefficient[j][i] / coefficient[i][i];
			coefficient[j][i] = 0
			for k in range(i + 1, size):
				coefficient[j][k] -= coefficient[i][k] * scalingFactor
			augmented[j] -= augmented[i] * scalingFactor

	# Calculating the result by back substitution
	for i in reversed(range(size)):
		total = 0
		for j in range(i + 1, size):
			total += coefficient[i][j] * augmented[j];
		augmented[i] = (augmented[i] - total) / coefficient[i][i]

	return augmented

def rowEchelon(inputMatrix):
	'''
	This function returns the row Echelon form of the matrix in the most optimal way.
	'''

	# Copying the matrix so that the original matrix does not change
	matrix = copy.copy(inputMatrix)

	########## CHECKING THE DIMENSIONS OF MATRIX #############

	if (rows := len(matrix)) == 0:
		raise TypeError("Empty Matrix")

	columns = len(matrix[0])

	# Checking if all rows have the same length
	for i in matrix[1:]: # Starting with second row because we are comparing it with the length of second row
		if len(i) != columns:
			raise TypeError("All rows of a matrix is of the same length")

	if columns == 0:
		raise TypeError("Length of rows should not be zero")

	######### CONVERTING THE MATRIX INTO ROW ECHELON FORM ##########

	# Keeps track of rows and columns
	row, column = 0, 0

	# This loops converts the matrix into row echelon form
	while row < rows and column < columns:

		# If pivot is equal to zero
		if matrix[row][column] == 0:

			# Searching for a non-zero number below a pivot
			for i in range(row + 1, rows):
				if matrix[i][column]:

					# Swapping the two rows
					matrix[row][j], matrix[i][j] = matrix[i][j], matrix[row][j]
					break

			# If there is no non-zero number below the pivot
			else:
				# Search in the next column
				column += 1
				continue

		#If pivot is not equal to zero
		else:
			for i in range(row + 1, rows):
				# If scaling factor is zero, then there will be no changes in the column
				if matrix[i][column] == 0:
					continue

				scalingFactor = matrix[i][column] / matrix[row][column]
				matrix[i][column] = 0
				for j in range(column + 1, columns):
					matrix[i][j] -= matrix[row][j] * scalingFactor

			# Going to the next pivotal
			row += 1
			column += 1

	return matrix

def reducedRowEchelon(inputMatrix):
	'''
	This function returns the reduced row echelon form of the matrix.
	'''

	# Copying the matrix so that the original matrix does not change
	matrix = copy.copy(inputMatrix)

	########## CHECKING THE DIMENSIONS OF MATRIX #############
		
	if (rows := len(matrix)) == 0:
		raise ValueError("Empty Matrix")

	columns = len(matrix[0])

	# Checking if all rows have the same length
	for i in matrix[1:]: # Starting with second row because we are comparing it with the length of second row
		if len(i) != columns:
			raise ValueError("All rows of a matrix is of the same length")

	######### CONVERTING THE MATRIX INTO REDUCED ROW ECHELON FORM ##########

	# Keeps track of rows and columns
	row, column = 0, 0

	# This loops converts the matrix into row echelon form
	while row < rows and column < columns:

		# If pivot is equal to zero
		if matrix[row][column] == 0:

			# Checking for a non-zero number below a pivot
			for i in range(row + 1, rows):
				if matrix[i][column]:

					# Swapping the two rows
					matrix[row], matrix[i] = matrix[i], matrix[row]
					break

			# If there is no non-zero number below the pivot
			else:
				# Search in the next column
				column += 1
				continue

		#If pivot is not equal to zero
		else:
			# Scaling the pivotal row to make the pivot equal to one
			scalingFactor = matrix[row][column]
			matrix[row][column] = 1
			for i in range(column + 1, columns):
				matrix[row][i] /= scalingFactor

			for i in range(rows):
				if i != row:
					# If scaling factor is zero, then there will be no changes in the column
					if matrix[i][column] == 0:
						continue

					scalingFactor = matrix[i][column]
					matrix[i][column] = 0
					for j in range(column + 1, columns):
						matrix[i][j] -= matrix[row][j] * scalingFactor

			row += 1
			column += 1

	return matrix

def rank(matrix):
	'''
	This function returns the rank of a matrix
	'''

	# Any error in the size of the matrix is dealt in the function rowEchelon itself
	# rowEchelon is used instead of reducedRow Echelon for more efficiency
	matrix = rowEchelon(matrix)

	rows = len(matrix)
	columns = len(matrix[0])

	rank = 0

	# Iterating over the matrix
	for i in range(rows):
		for j in range(columns):
			# If any number in the row is non-zero
			if matrix[i][j]:
				rank += 1
				break
		# If all numbers are zero, then exiting the loop
		else:
			break
	
	return rank
