# 438. Find All Anagrams in a String

s = "cbaebabacd" 
p = "abb"

# p is the word we are trying to find anagrams of within s
def find_anagrams(s, p):
    
    indices = []

    char_count = {}
    for char in p:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    start = 0
    end = len(p) - 1  # len(p) is the window size
    window_count = {}
    # first window
    for i in range(end + 1):
        if s[i] not in window_count:
            window_count[s[i]] = 0
        window_count[s[i]] += 1

    # Slide the window over s
    while end < len(s):
        if window_count == char_count:
            indices.append(start)
        
        start += 1
        end += 1

        if end < len(s):
            if s[end] not in window_count:
                window_count[s[end]] = 0
            window_count[s[end]] += 1
        
        window_count[s[start - 1]] -= 1
        if window_count[s[start - 1]] == 0:
            del window_count[s[start - 1]]


    return indices

print(find_anagrams(s, p))
