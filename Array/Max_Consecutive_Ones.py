"""
Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""
Input = [1,1,0,1,1,1,0,1,0,1,1,1,1]


def findMaxConsecutiveOnes(nums):
    count = 0
    result = 0 
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            print("Found Consecutive Ones : ", count)
            result = max(result,count)                    #count maximum
        else:
            count = 0                                     #Reset
    
    return result


max_consec = findMaxConsecutiveOnes(Input)
print(max_consec)