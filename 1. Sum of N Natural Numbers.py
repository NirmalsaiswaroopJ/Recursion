# Recursion problem 1
# Sum of N Natural Numbers

def sum_of_n_natural(number):
    if number == 0:
        return 0
    else:
        return number + sum_of_n_natural(number - 1)
    
