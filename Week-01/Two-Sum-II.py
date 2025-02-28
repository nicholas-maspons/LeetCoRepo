# 167. Two Sum II - Input Array Is Sorted

numbers = [-1, 0]
target = -1

def two_sum(numbers, target):
    
    left = 0
    right = len(numbers) - 1

    while left < right:
        # summ since sum is a built-in function
        summ = numbers[left] + numbers[right]    
        if summ < target:
            left += 1
        elif summ > target:
            right -= 1
        else:
            return [left + 1, right + 1]
    
    return []

print(two_sum(numbers, target))

