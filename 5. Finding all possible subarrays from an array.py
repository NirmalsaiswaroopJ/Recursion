# Recursion problem 5
# Finding all possible subsets of an array using recursion

def all_subarray(arr, index, temp):
    if index >= len(arr):
        print(temp)
        return
    temp.append(arr[index])
    all_subarray(arr, index + 1, temp)
    temp.pop()
    all_subarray(arr, index + 1, temp)


