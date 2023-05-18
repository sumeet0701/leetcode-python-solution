"""
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""
def isPalindromeNumber(number):
    lst = [digit for digit in str(number)]
    index =0
    for i in lst:
        if i != lst[-index-1]:
            return False
        index+=1
    return True
a = -121
print(isPalindromeNumber(a))


