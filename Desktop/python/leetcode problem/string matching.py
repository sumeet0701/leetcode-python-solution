"""
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Input: words = ["blue","green","bu"]
Output: []

"""

words = ['mass','as','superhero', 'hero','super']

result =[]
index =0

while index<len(words):
    word = words[index]
    for i in range(len(words)):
        if i ==index:
            continue
        if word in words[i]:
            if word not in result:
                result.append(word)
    index +=1
print(result)