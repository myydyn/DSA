# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
    # Input: strs = ["eat","tea","tan","ate","nat","bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
    # There is no string in strs that can be rearranged to form "bat".
    # The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    # The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
    # Input: strs = [""]
    # Output: [[""]]
# Example 3:
    # Input: strs = ["a"]
    # Output: [["a"]]
# Constraints:
    # 1 <= strs.length <= 104
    # 0 <= strs[i].length <= 100
    # strs[i] consists of lowercase English letters.


from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: str) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Chuyển danh sách count thành một tuple (vì tuple có thể làm khóa cho từ điển)
            # và thêm chuỗi s vào danh sách các từ hoán vị tương ứng trong từ điển res.
            # lúc này trong từ điển có các khóa là chuỗi đếm số lần xuất hiện của mỗi ký tự c trong từ s
            # vd: (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
            # từ nào có chuỗi đếm giống nhau thì vào chung 1 nhóm
            res[tuple(count)].append(s)
        return res.values()

    def groupAnagrams2(self, strs: str) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
            # [sorted_word] không phải là danh sách mà là cách truy cập một mục (entry) trong từ điển. 
            # sorted_word là một chuỗi (đại diện cho các từ sau khi sắp xếp), và ta dùng nó làm khóa
        return list(anagram_map.values())



if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    
    print(Solution().groupAnagrams2(strs))  
