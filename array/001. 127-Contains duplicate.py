from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

    # Cach2:
    # return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 1]
    print(type(nums))  # In ra kiểu dữ liệu của nums (list)
    print(Solution().containsDuplicate(nums))  # Gọi hàm containsDuplicate
