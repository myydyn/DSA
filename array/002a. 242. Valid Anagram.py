from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # hai dictionary dùng để lưu số lần xuất hiện của mỗi ký tự trong s và t.
        # Dictionary trong Python cho phép lưu trữ cặp giá trị key:value, trong đó key là KÝ TỰ và value là số lần xuất hiện của ký tự đó.
        countS, countT = {}, {}

        for i in range(len(s)):
            # Vòng lặp chạy từ i = 0 đến i = len(s) - 1 (tức là duyệt qua tất cả các ký tự của chuỗi s và t).
            # Ở mỗi bước của vòng lặp, code xử lý lần lượt ký tự thứ i của cả hai chuỗi s[i] và t[i].
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
#         Ví dụ:
# Với chuỗi s = 'anagram':
# Ở bước đầu tiên (i = 0), s[0] = 'a'. Ký tự 'a' chưa có trong countS, nên get('a', 0) trả về 0. Sau đó, nó cộng thêm 1 và lưu vào countS, kết quả là countS = {'a': 1}.
# Khi gặp lại 'a' ở bước sau (i = 2), giá trị hiện tại của 'a' trong countS là 1, nên get('a', 0) trả về 1 và sau đó cộng thêm 1, dẫn đến countS = {'a': 2}.

        for c in countS:
            # Lấy số lần xuất hiện của ký tự c trong countT. Nếu ký tự này không tồn tại trong countT (tức là chuỗi t không chứa ký tự đó), trả về 0.
            if countS[c] != countT.get(c, 0):
                return False
        return True



if __name__ == "__main__":
    s = 'rat'
    t = 'car'
    
    print(Solution().isAnagram(s, t)) 