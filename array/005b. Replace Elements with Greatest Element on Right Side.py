from typing import List


class Solution:
    def replaceElements(self, arr):
        out = [-1] #yeu cau gan -1 cho vi tri cuoi cung
        max = 0 # constraints la so duong
        for i in arr[::-1]:
            if max < i:
                max = i
            out.append(max)
        out.pop()    #The pop() method removes (pops) the last element of an array.
        return out[::-1]



if __name__ == "__main__":
    arr = [17,18,5,4,6,1]
    print(len(arr))  
    print(Solution().replaceElements(arr)) 
