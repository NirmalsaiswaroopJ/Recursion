# Recursion problem 4
# To check if a string is a Palindrome or not by recursion

def recursive_palindrome_string(string, left, right):
    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return recursive_palindrome_string(string, left + 1, right - 1)

