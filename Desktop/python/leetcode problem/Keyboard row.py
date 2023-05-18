"""
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Input: words = ["omk"]
Output: []

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

leetcode link = https://leetcode.com/problems/keyboard-row/

"""
def FindOutWord(words):
    output = []
    for word in words:
        value = set(word.lower())
        if value <= set("qwertyuiop") or value <= set("asdfghjkl") or value <= set("zxcvbnm"):
            output.append(word)
    return output
words = ["Hello","Alaska","Dad","Peace"]
print(FindOutWord(words))