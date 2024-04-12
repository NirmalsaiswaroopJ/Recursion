# Recursion problem 7.
# Find all possible combinations of k numbers out of the range 1 to N using recurion.

def possible_combination(n, k):
    result = []
    def backtrack(start, combo):
        if len(combo) == k:
            result.append(combo[:])
            return
        for i in range(start, n+1):
            combo.append(i)
            backtrack(i+1, combo)
            combo.pop()
        return result
    for j in range(1,n+1):
        backtrack(j, [])
    temp = []
    for i in result:
        if i in temp:
            continue
        else:
            temp.append(i)
    return temp

