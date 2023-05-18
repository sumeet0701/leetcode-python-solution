'''
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.


Input: words1 = ["b","bb","bbb"], words2 = ["b","bb","bbb"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".


'''
def countWords(words1, words2) -> int:
    count1, count2 = Counter(words1), Counter(words2)
    return len({i for i, j in count1.items() if j == 1} & {i for i, j in count2.items() if j == 1})

words1 = ["a","ab"]
words2 = ["a","a","a","ab"]

print(countWords(words1,words2))