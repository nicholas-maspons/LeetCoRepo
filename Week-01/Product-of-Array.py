# 238. Product of Array Except Self

nums = [1, 2, 3, 4]

def product_of_array(numbers):

    left = []  # l -> r
    right = []  # l <- r
    answer = []

    product = 1
    for i in range(len(numbers)):
        product *= numbers[i]
        left.append(product)

    product = 1
    for i in range(-1, - len(numbers) - 1, -1):
        product *= numbers[i]
        right.append(product)
    right.reverse()
    
    for i in range(len(numbers)):
        if i == 0:
            answer.append(right[i + 1])
        elif i == len(numbers) - 1:
            answer.append(left[i - 1])
        else:
            answer.append(left[i - 1] * right[i + 1])

    return answer

print(product_of_array(nums))
