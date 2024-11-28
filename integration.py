import numpy as np

def Trapezoid_Integration(function, lowerBound, upperBound, trapezium):
	'''
	This function returns the value of integration from lower bound to upper bound
	by calculating the areas of trapezium formed between the two points.
	'''

	# If number of trapeziums is less than zero, then an error is generated
	if trapezium <= 0:
		raise ValueError("Number of trapeziums must be greater than 0.")

	# To create n consecutive trapeziums, n + 1 points are required
	# np.linspace returns an numpy array of specific amount of integers
	# between two numbers including them
	points = np.linspace(lowerBound, upperBound, trapezium + 1)

	# length between two points
	# serves as height of trapezium
	intervalLength = (upperBound - lowerBound) / trapezium

	integralValue = 0

	# Calculating the length of sides first trapezium
	lengthLeftSideTrapezium = function(points[0])
	lengthRightSideTrapezium = function(points[1])

	# area of a trapezium
	integralValue += 0.5 * (lengthLeftSideTrapezium + lengthRightSideTrapezium) * intervalLength

	for i in range(1, trapezium):

		# Instead of again calculating the value of two sides,
		# the left side of next trapezium will be equal to right side of next trapezium
		# Only the length of one side of trapezium is required
		# For this, we calculated the value of first two sides outside the loop
		lengthLeftSideTrapezium = lengthRightSideTrapezium
		lengthRightSideTrapezium = function(points[i + 1])
		integralValue += 0.5 * (lengthLeftSideTrapezium + lengthRightSideTrapezium) * intervalLength

	return integralValue

def Rectangle_Integration(function, lowerBound, upperBound, rectangle):
	'''
	This function returns the value of integration from lower bound to upper bound
	by calculating the areas of rectangle formed between the two points.
	'''

	# If number of rectangles is less than zero, then an error is generated
	if rectangle <= 0:
		raise ValueError("Number of rectangles must be greater than 0.")

	# To create n consecutive rectangles, n + 1 points are required
	# np.linspace returns an numpy array of specific amount of integers
	# between two numbers including them
	points = np.linspace(lowerBound, upperBound, rectangle + 1)

	# length between two points
	# serves as breadtht of rectangle
	intervalLength = (upperBound - lowerBound) / rectangle

	integralValue = 0

	# Calculating the length of sides first rectangle
	lengthLeftSideRectangle = function(points[0])
	lengthRightSideRectangle = function(points[1])

	# area of a rectangle
	integralValue += 0.5 * (lengthLeftSideRectangle + lengthRightSideRectangle) * intervalLength

	for i in range(1, rectangle):

		# Instead of again calculating the value of two sides,
		# the left side of next rectangle will be equal to right side of next rectangle
		# Only the length of one side of rectangle is required
		# For this, we calculated the value of first two sides outside the loop
		lengthLeftSideRectangle = lengthRightSideRectangle
		lengthRightSideRectangle = function(points[i + 1])
		integralValue += 0.5 * (lengthLeftSideRectangle + lengthRightSideRectangle) * intervalLength

	return integralValue
