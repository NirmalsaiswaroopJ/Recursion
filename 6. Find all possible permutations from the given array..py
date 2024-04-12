# Recursion problem 6.
# Find all the permutations of an array using recursion

def all_permutation(array, start = 0, result = None):
    if result == None:
        result = []
    if start == len(array):
        result.append(array[:])
        return
    for i in range(start, len(array)):
        array[start], array[i] = array[i], array[start]
        all_permutation(array, start + 1, result)
        array[start], array[i] = array[i], array[start]
    return result

