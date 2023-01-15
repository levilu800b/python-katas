# Write a function that takes an array of integers as input and returns the smallest integer in the array.

# When the array is empty or None, return 0.

# Note: The function should also work with negative numbers.

# For example:

# findSmallestInt([78, 56, 232, 12, 11, 43]) returns 11
# findSmallestInt([78, 56, -2, 12, 8, -33]) returns -33
# findSmallestInt([0, 1-2**64, 2**64]) returns 1-2**64

# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def findSmallestInt(arr):
    if arr is None:
        return 0
    else:
        arr.sort()
        return arr[0]

print(findSmallestInt([78, 56, 232, 12, 11, 43]))