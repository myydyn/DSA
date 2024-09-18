from typing import List
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # defaultdict là một loại từ điển đặc biệt trong Python, giống với dict, nhưng với một điểm khác biệt: nếu bạn truy cập một khóa (key) không tồn tại trong từ điển, thay vì gây ra lỗi KeyError, nó sẽ tự động tạo một mục mới cho khóa đó với giá trị mặc định do bạn chỉ định.
        # Khi bạn truyền int làm đối số cho defaultdict, nó không phải là số nguyên cụ thể, mà là hàm int(). Hàm này khi được gọi mà không có đối số sẽ trả về giá trị mặc định là 0.
        # count = defaultdict(int) có nghĩa là count là một từ điển mà nếu bạn truy cập vào một khóa không tồn tại, nó sẽ tự động gán cho khóa đó giá trị mặc định là 0.
        count = defaultdict(int)
        for i in s:
            count[i] += 1

        for i in t:
            count[i] -= 1
        
        # count là một từ điển mà các khóa là các ký tự xuất hiện trong hai chuỗi s và t, còn các giá trị (chính là val) là số lần xuất hiện của mỗi ký tự trong chuỗi s trừ đi số lần xuất hiện của ký tự đó trong chuỗi t.
        for value in count.values():
            if value != 0:
                return False
        return True
        



if __name__ == "__main__":
    s = 'banana'
    t = 'anaban'
    
    print(Solution().isAnagram(s, t)) 