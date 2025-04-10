# 394. Decode String

class Solution(object):
    def decodeString(self, s):
        string_stack = []
        number_stack = []
        decoded = ""

        is_number = False
        for char in s:
            if char.isdigit():
                number_stack.append(char)
            elif char == "[":
                string_stack.append(decoded)
                decoded = ""
            elif char == "]":
                times = int(number_stack.pop())
                sub_string = decoded * times
                decoded = string_stack.pop() + sub_string
            else:
                decoded += char
        
        return decoded

solution = Solution()
print(solution.decodeString("3[a]2[bc]"))