# 75. Sort Colors

nums = [2, 0, 2, 1, 1, 0]

def sort_colors(lst):

    zeros, ones, twos = 0, 0, 0

    for i in lst:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1
        elif i == 2:
            twos += 1
    
    index = 0

    while zeros > 0:
        lst[index] = 0
        zeros -= 1
        index += 1

    while ones > 0:
        lst[index] = 1
        ones -= 1
        index += 1

    while twos > 0:
        lst[index] = 2
        twos -= 1
        index += 1

    return lst

print(sort_colors(nums))
