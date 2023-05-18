'''
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

'''

names = ["Alice","Bob","Bob"]
heights =[155,185,150]
'''
heights_names = {}
for i in range(len(names)):
	heights_names[heights[i]] = names[i]
sorted_ = dict(sorted(heights_names.items(),reverse = True))
output = []
for height in sorted_:
	output.append(sorted_[height])
print(output)
'''

sorted1 = dict(zip(names,heights))
print(sorted1)
