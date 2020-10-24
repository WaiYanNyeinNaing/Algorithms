"""
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
"""

nums = [12,345,2,6,7896]

def findNumbers(nums):
    count = 0
    result = 0
    for i in range(len(nums)):
        nums[i] = str(nums[i])
        if len(nums[i]) % 2 == 0:
            count += 1
            # result = max(result,count)
            
    return count


print(findNumbers(nums))