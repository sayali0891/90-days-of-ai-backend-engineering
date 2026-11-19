"""
Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
"""

def concatenateArr(nums):
    initialLen = len(nums)
    print(f"Initial len is {initialLen}")
    for i in range(0,initialLen):
        print(f"i : {i} , val : {nums[i]}")
        nums.append(nums[i])
    return nums

if __name__ == "__main__":
    print(f"Result : {concatenateArr([1,2,1])}")