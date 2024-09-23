# 58. Length of Last Word
    # Given a string s consisting of words and spaces, return the length of the last word in the string.
    # A word is a maximal substring consisting of non-space characters only.

    # Example 1:
    #     Input: s = "Hello World"
    #     Output: 5
    #     Explanation: The last word is "World" with length 5.
    # Example 2:
    #     Input: s = "   fly me   to   the moon  "
    #     Output: 4
    #     Explanation: The last word is "moon" with length 4.
    
    # Constraints:
    #     1 <= s.length <= 104
    #     s consists of only English letters and spaces ' '.
    #     There will be at least one word in s.


from typing import List

class Solution:
    def lengthOfLastWord(self, s):
        # xét từng ký tự trong s
        i, length = len(s)-1, 0
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
        


        
if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    print(len(s))
    # s = " m "
    print(Solution().lengthOfLastWord(s))  
