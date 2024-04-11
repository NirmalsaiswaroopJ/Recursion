# Recursion problem 3
# Find the Nth power of a number using recursion

def nth_power_of_number(power, number):
    if power == 0:
        return 1
    else:
        return number * nth_power_of_number(power-1, number)

    
