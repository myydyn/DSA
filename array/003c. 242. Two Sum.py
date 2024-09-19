from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: int, target: int) -> list[int]:
        numsMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numsMap:
                return [numsMap[complement], i]
            numsMap[nums[i]] = i

        return


if __name__ == "__main__":
    nums = [2,15,11,7] 
    target = 9
    print(type(nums))
    print(Solution().twoSum(nums, target)) 