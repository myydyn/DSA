# 14. Longest Common Prefix
    # Write a function to find the longest common prefix string amongst an array of strings.
    # If there is no common prefix, return an empty string "".

    # Example 1:
        # Input: strs = ["flower","flow","flight"]
        # Output: "fl"
    # Example 2:
        # Input: strs = ["dog","racecar","car"]
        # Output: ""
        # Explanation: There is no common prefix among the input strings.


from typing import List

class Solution:
    def longestCommonPrefix(self, strs):
        sult = ""
        # phần tử đầu tiên của chuỗi là flower làm mốc, cho i chạy qua từng vị trí ký tự của các phần tử
        # nếu đều giống các ký tự của mốc thì cho ra kết quả
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return sult
            sult += strs[0][i]
        return sult
        

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))  
