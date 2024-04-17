# Recursion problem 8
# 8. Letter Combinations of a Phone Number by Recursion

def letter_combinations(phone_number):
    result = []
    letter_dict = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z')
    }
    def backtrack(index,path):
        if len(path) == len(phone_number):
            result.append("".join(path))
            return
        digit = phone_number[index]
        letters = letter_dict[digit]
        for letter in letters:
            path.append(letter)
            backtrack(index+1,path)
            path.pop()
    if len(phone_number) == 0:
        return []
    backtrack(0,[])
    return result


        
