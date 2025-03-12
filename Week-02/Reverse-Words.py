# 151. Reverse Words in a String

s = "  hello world  "

# Im not proud of this
def reverse_words(s):
    
    words = s.strip().split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

print(reverse_words(s))
