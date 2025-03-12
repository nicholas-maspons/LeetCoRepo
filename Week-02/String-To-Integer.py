# 8. String to Integer (atoi)

s = "42"
s = "     -042"
# s = "1337c0d3"
# s = "0-1"
# s = "words and 987"


def myAtoi(s):
    start = False
    number = []  

    for char in s:
        # print(char)
        
        if (not start) and not char.isdigit() and char not in "+- ":
            # print("return 1")
            return 0
        elif start and (not char.isdigit()):
            # print("return 2")
            return int("".join(number))
        elif char.isdigit() or char in "+-":  # len of "+-" is constant
            start = True
            number.append(char)
        
    return int("".join(number))  # when the final char is also part of the number
    
    
print(myAtoi(s))
