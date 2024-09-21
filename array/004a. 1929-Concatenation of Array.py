# 1929. Concatenation of Array
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Constraints:
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000


from typing import List


class Solution:
    def Concatenation_Array(self, nums: List[int]):
        # CACH 1: plus or multiply
        # return nums + nums

        # CACH 2: append
        # answer = []
        # for i in range(2):
        #     for n in nums:
        #         answer.append(n)
        # return answer
        
        # CACH 3: extend
        # ans = nums
        # ans.extend(nums)
        # return ans
    
        # CACH 4: [2*len(nums)]
        n = len(nums)
        ans = [0]*2*n # create a blank lst sz 2n
        for i in range(n):
            ans[i] = nums[i]  #copy 1st part
            ans[i+n] = nums[i] # copy 2nd part
        return ans



if __name__ == "__main__":
    nums = [1, 2, 1]
    print(Solution().Concatenation_Array(nums)) 

