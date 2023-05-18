'''
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".

Input: s = "What is the solution to this problem", k = 4
Output: "What is the solution"
Explanation:
The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".

Input: s = "chopper is not a tanuki", k = 5
Output: "chopper is not a tanuki"
'''

s = "Hello how are you Contestant"
k = 4;
empty= []
for i in range(len(s.split())):
    if i ==k:
        break
    empty.append(s.split()[i])
result =' '.join(empty)
print(result)