# Recursion problem 2
# Finding the Nth term in the Fibonacci series

def nth_fibonacci_term(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        ans1 = nth_fibonacci_term(n-1)
        ans2 = nth_fibonacci_term(n-2)
        return ans1 + ans2

