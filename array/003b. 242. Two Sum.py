from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: int, target: int) -> list[int]:
        # prevMap = {}: Khai báo một từ điển trống prevMap, sẽ dùng để lưu các số đã được duyệt qua trong nums, với val là giá trị trong danh sách và index là chỉ số của giá trị đó.
        prevMap = {} #val:index
        # Hàm enumerate(nums) lấy chỉ số của phần tử (được gán cho biến i), va lấy giá trị của phần tử (được gán cho biến n).
        # vd: Chỉ số: 0, Giá trị: 2 (i=0; n=2)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap: #diff là giá trị
                return [prevMap[diff], i] # trả về chỉ số của diff, i là chỉ số
            prevMap[n] = i #chưa có thì gán chỉ số của n = i, lucs này thì prevMap là dict chứa{n:i, ...} 
        return


if __name__ == "__main__":
    nums = [2,15,7,11] 
    target = 9
    print(type(nums))
    print(Solution().twoSum(nums, target)) 