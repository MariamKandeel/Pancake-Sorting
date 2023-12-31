# -*- coding: utf-8 -*-
"""pancake sorting

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1erCc7mHNBot41U4UfKWYa2Q0A3n-iPTS
"""

# pancake sort

# Reverses arr[0..i]
def flip(arr, i):
	start = 0
	while start < i:
		temp = arr[start]
		arr[start] = arr[i]
		arr[i] = temp
		start += 1
		i -= 1



# Returns index of the maximum

def findMax(arr, n):
	mi = 0
	for i in range(0, n):
		if arr[i] > arr[mi]:
			mi = i
	return mi

# The main function that
# sorts the given array
# using flip operations
def pancakeSort(arr, n):
	# Start from the complete
	# array and reduce
	# the current size
	curr_size = n
	while curr_size > 1:
		# Find the index of the maximum
		# element in arr[0..curr_size-1]
		mi = findMax(arr, curr_size)

		# Move the maximum element
		# to the end of the current array
		# if it's not already at the end
		if mi != curr_size - 1:
			# To move it to the end,
			# first move the maximum number
			# to the beginning
			flip(arr, mi)
			printArray(arr, n)
			print()

			# Now move the maximum number
			# to the end by reversing
			# the current array
			flip(arr, curr_size - 1)
			printArray(arr, n)
			print()

		curr_size -= 1

    #DECREASE BY FACTOR OF 1 START


# A utility function to
# print an array of size n
def printArray(arr, n):
	for i in range(0, n):
		print("%d" % (arr[i]), end=" ")
	print()

# Driver program
arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)

print("Original Array")
printArray(arr, n)
print()

print("Sorting Steps")
pancakeSort(arr, n)

print("Sorted Array")
printArray(arr, n)