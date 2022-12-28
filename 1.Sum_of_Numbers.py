"""
This code explains the index of the two number, which makes the total of a given target number.
Assumptions:
    1. There will be only one possible solution
    2. Repeated numbers are also considered. e.g. [3,3] = 6, indexes=[0,1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if i<= target:
                for j in range(nums.index(i)+1,len(nums)):
                    if i+nums[j] == target:
                            return [nums.index(i), j]
            else:
                pass
        return -1

s = Solution()
k = s.twoSum([0,2,5,4,0], 0)
if k== -1:
    print("Enter a valid data")
else:
    print(k)