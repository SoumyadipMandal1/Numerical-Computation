import numpy as np

def trapezoid(function, lowerBound, upperBound, trapezium):
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

def rectangle(function, lowerBound, upperBound, rectangles):
	'''
	This function returns the value of integration from lower bound to upper bound
	by calculating the areas of rectangle formed between the two points.
	'''

	# If number of rectangles is less than zero, then an error is generated
	if rectangles <= 0:
		raise ValueError("Number of rectangles must be greater than 0.")

	# To create n consecutive rectangles, n + 1 points are required
	# np.linspace returns an numpy array of specific amount of integers
	# between two numbers including them
	points = np.linspace(lowerBound, upperBound, rectangles + 1)

	# length between two points
	# serves as breadtht of rectangle
	intervalLength = (upperBound - lowerBound) / rectangles

	# Let midpoint1, midpoint2, ..., midpointn, be the midpoints of rectangle1,
	# rectangle2, ..., rectanglen respectively
	# integralValue  = midpoint1 * intervalLength + midpoint2 * intervalLength
	#                  + ... + midpointn * intervalLength
	# integralValue = (midpoint1 + midpoint2 + ... + midpointn) * intervalLength

	integralValue = 0
	for i in range(rectangles):
		integralValue += (function(points[i]) + function(points[i + 1])) / 2
	integralValue *= intervalLength

	return integralValue

def simpson(function, lowerBound, upperBound, rectangles):
	"""
	This function returns the value of Simpson integration
	"""

	# If number of rectangles is less than zero, then an error is generated
	if rectangles <= 0:
		raise ValueError("Number of rectangles must be greater than 0.")

	# Width of each bin
	rectWidth = (upperBound - lowerBound) / rectangles
	rectWidth /= 3

	# Creating points
	points = np.linspace(lowerBound, upperBound, rectangles + 1)
	function_value = []
	for i in points:
		function_value.append(function(i))

	function_value = np.array(function_value)
	function_value[::2] *= 2
	function_value[1::2] *= 4
	function_value[0] /= 2
	function_value[-1] /= 2
	function_value *= rectWidth

	return sum(function_value)
