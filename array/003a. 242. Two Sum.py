from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums, target) -> bool:
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n-1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return


if __name__ == "__main__":
    nums = [2,15,7,11] 
    target = 9
    
    print(Solution().twoSum(nums, target)) 